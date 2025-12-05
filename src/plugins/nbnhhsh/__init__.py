from nonebot import get_plugin_config, logger, on_regex
from nonebot.plugin import PluginMetadata
from nonebot.params import RegexStr
from nonebot.adapters import Event  # [新增] 引入 Event 以获取用户ID
import httpx
import re
import time  # [新增] 引入 time 模块

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="[ 缩写翻译 ] 能不能好好说话 - nbnhhsh",
    description="能不能好好说话 - 使用神奇海螺api查询 @qingzhixing",
    usage="[缩写英文]是什么|是啥",
    config=Config,
    type="application",
    homepage="https://github.com/qingzhixing/nonebot-plugin-nbnhhsh-q",
    supported_adapters=None,
)

# 输出插件加载日志
logger.info("插件 nbnhhsh 已加载")

#regular_expression = r"[a-z0-9]{2,}(?:是什么|是啥)"
regular_expression = r".*(是什么|是啥)$"

config = get_plugin_config(Config)

nbnhhsh_macher = on_regex(
    regular_expression, priority=10, block=True, flags=re.IGNORECASE
)

# [新增] 配置冷却时间（秒）
COOLDOWN_SECONDS = 10
# [新增] 用于存储用户最后请求时间的字典
user_last_request = {}

@nbnhhsh_macher.handle()
async def handle_nbnhhsh(event: Event, keyword: str = RegexStr()): # [修改] 添加 event 参数
    global user_last_request

    # [新增] --- 冷却时间检查逻辑开始 ---
    user_id = event.get_user_id()
    current_time = time.time()

    # 清理过大的缓存防止内存泄漏（仿照下方 Guess 的逻辑）
    if len(user_last_request) > 1024:
        user_last_request = {}

    if user_id in user_last_request:
        time_diff = current_time - user_last_request[user_id]
        if time_diff < COOLDOWN_SECONDS:
            logger.info(f"用户 {user_id} 请求过快，剩余冷却: {COOLDOWN_SECONDS - time_diff:.2f}s")
            # 这里可以选择直接 return 忽略，或者发送提示
            # await nbnhhsh_macher.finish(f"歇一歇吧，请 {int(COOLDOWN_SECONDS - time_diff)} 秒后再试。")
            await nbnhhsh_macher.finish() # 直接结束，不回复，避免刷屏
            return

    # 更新该用户的最后请求时间
    user_last_request[user_id] = current_time
    # [新增] --- 冷却时间检查逻辑结束 ---

    logger.info(f"原始 keywordGroup: {keyword}")

    keyword_string = keyword.replace("是什么", "").replace("是啥", "")
    logger.info(f"nbnhhsh keyword: {keyword_string}")
    # 调用神奇海螺api查询
    result_dict = await query_nbnhhsh(keyword_string)

    # 发送查询结果
    if result_dict and "name" in result_dict:

        reply_string = f"{keyword_string} 可能是:\n"
        if "trans" in result_dict and result_dict["trans"]:

            results = result_dict["trans"]
            if len(results) == 1:
                reply_string += results[0]
            else:
                # 添加 "或者"
                reply_string += "\n".join(results[:-1]) + "，" + results[-1]

        else:
            reply_string = f"没能找到 {keyword_string} 的含义"

    else:
        reply_string = f"没能找到 {keyword_string} 的含义"
    await nbnhhsh_macher.send(reply_string)


NBNHHSH_API_URL = "https://lab.magiconch.com/api/nbnhhsh/"

Guess = {}


async def query_nbnhhsh(keyword: str) -> dict:
    global Guess  # 声明使用全局变量 Guess

    # 如果Guess字典大小大于1024，则清空它
    if len(Guess) > 1024:
        Guess = {}

    # 提取关键词中的字母数字组合，长度至少为2
    if not keyword:
        return {}

    if Guess.get(keyword):
        logger.info(f"使用缓存结果: {Guess[keyword]}")
        return Guess[keyword]

    try:
        # 发送POST请求
        async with httpx.AsyncClient() as client:
            response = await client.post(
                NBNHHSH_API_URL + "guess",
                json={"text": keyword},
                headers={"Content-Type": "application/json"},
                timeout=10,  # 设置超时时间
            )

            # 解析响应
            data = response.json()
            if data and len(data) > 0:
                Guess[keyword] = data[0]
                return data[0]
            else:
                return {}

    except httpx._exceptions.RequestError as e:
        logger.error(f"请求出错: {e}")
        return {}
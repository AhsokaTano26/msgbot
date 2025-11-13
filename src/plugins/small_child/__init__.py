from apscheduler.triggers.cron import CronTrigger
from nonebot import get_plugin_config, on_command, require, logger, get_driver, on_notice
from nonebot.adapters.onebot.v11 import GroupMessageEvent, PokeNotifyEvent, MessageSegment
from nonebot.plugin import PluginMetadata
import random
import requests
from .config import Config
import nonebot
import asyncio
from datetime import datetime, timedelta
from typing import Dict, Tuple

nonebot.init(command_start={"", ""}, command_sep={".", " "})

__plugin_meta__ = PluginMetadata(
    name="small_child",
    description="",
    usage="",
    config=Config,
)
plugin_config = get_plugin_config(Config)

async def ignore_group(event: GroupMessageEvent) -> bool:
    """检查是否在忽略的群中"""
    a = int(event.group_id)
    if a in plugin_config.ignored_groups:
        return False
    return True

small_child1 = on_command("渡月", priority=10,rule=ignore_group)
small_child2 = on_command("jsylx", aliases={"神人"},priority=10,rule=ignore_group)
small_child3 = on_command("富哥",aliases={"有钱"}, priority=10,rule=ignore_group)
small_child4 = on_command("佑佑姐", aliases={"佑佑"},priority=10,rule=ignore_group)
small_child5 = on_command("Shion", aliases={"ako酱"},priority=10,rule=ignore_group)
small_child6 = on_command("卡顺米",priority=10,rule=ignore_group)
small_child7 = on_command("一二",priority=10,rule=ignore_group)
small_child8 = on_command("tano",priority=10,rule=ignore_group)

@small_child1.handle()
async def handle_rss(event: GroupMessageEvent):
    msg = ["渡月是好人吗？",
           "渡月仁善暖人心\n真的吗？",
           "渡月赤诚又热忱",
           "渡月良善若暖阳",
           "渡月是大坏蛋！",
           "渡月天天欺负tano",
           "渡月纯真好楷模",
           "今天吃什么",
           "又在吃好的了",
           "羡慕了富哥",
           "渡月带带我",
           "富哥",
           "哎，资本",
           "吃播系列"
    ]
    send_msg = random.choice(msg)
    await small_child1.send(send_msg)

@small_child2.handle()
async def handle_rss(event: GroupMessageEvent):
    msg = ["jsylx怎么这么坏啊",
           "最爱一二了",
           "desuwa",
           "jsylx是个大坏蛋",
           "jsylx真好啊",
           "jsylx怎么天天欺负小孩",
           "jsylx怎么天天欺负群u",
           "jsylx 实在很糟糕",
           "esua",
           "狂言震碎三观"
    ]
    send_msg = random.choice(msg)
    await small_child2.send(send_msg)

@small_child3.handle()
async def handle_rss(event: GroupMessageEvent):
    msg = ["慕了"]
    send_msg = random.choice(msg)
    await small_child3.send(send_msg)

@small_child4.handle()
async def handle_rss(event: GroupMessageEvent):
    msg = ["是坏蛋美人哟❥(^_-)","是个小笨蛋捏","佑佑姐人美心善"]
    send_msg = random.choice(msg)
    await small_child4.send(send_msg)
    # num = random.randint(1, 1000)
    # if num <= 200:
    #     await small_child4.send("是坏蛋美人哟❥(^_-)")
    # elif 350 <= num <= 450:
    #     await nonebot.get_bot().set_group_ban(
    #         group_id=1016925587,
    #         user_id=1774796963,
    #         duration=0
    #     )

@small_child5.handle()
async def handle_rss(event: GroupMessageEvent):
    msg = ["是ako大神哟",
           "卖萌",
           "唔……人家真的有在好好练习打鼓啦，才不是偷懒哦。要是前辈们能多夸夸亚子就好啦，拜托拜托嘛~",
           "唔姆… 别闹啦，弦都差点松了哦（鼓腮"
           ]
    send_msg = random.choice(msg)
    await small_child5.send(send_msg)

@small_child6.handle()
async def handle_rss(event: GroupMessageEvent):
    msg = ["看看ksar",
           "esua",
           "desuwa",
           "最爱jsylx了"
    ]
    send_msg = random.choice(msg)
    await small_child6.send(send_msg)

@small_child7.handle()
async def handle_rss(event: GroupMessageEvent):
    msg = ["最爱jsylx了",
           "已经不能离开jsylx了",
           "jsylx是我臭宝宝",
           "jsylx你是我无二的例外"
    ]
    send_msg = random.choice(msg)
    await small_child7.send(send_msg)

@small_child8.handle()
async def handle_rss(event: GroupMessageEvent):
    msg = [
        "我是tano",
        "你在期待什么？",
        "又被渡月欺负了",
        "tano是个大笨蛋",
        "我是穷逼"
    ]
    send_msg = random.choice(msg)
    await small_child7.send(send_msg)



# 全局冷却记录器 - 格式: {用户ID: 最后响应时间}
cooldown_records: Dict[int, datetime] = {}

# 获取机器人配置
driver = get_driver()
try:
    bot_self_id = driver.config.self_id
except:
    bot_self_id = None

msg = ["请不要戳我！",
               "痒痒的哦… 要不要摸摸我的耳朵呀？",
               "喂、喂… 突然戳过来算什么啊！",
               "突然戳我做什么！笨蛋人类！",
               "别、别乱碰啊… 我可不是随便让人摸的！",
               "喂喂，戳之前先打报告啊！",
               "谁、谁允许你碰我的… 哼！",
               "再戳就、就咬你了哦！",
               "笨手笨脚的… 戳得我耳朵都痒了！",
               "说过多少次别随便碰我… 笨蛋！",
               "突然戳过来… 吓、吓到我了啦！",
               "下不为例啊… 绝对没有下次！",
               "被jsylx做局了",
               "aiai",
               "biubiu~ 发射可爱光线击中你啦！",
               "要抱抱充电吗？kkr电力超足～",
               "笨蛋！手没地方放就去抓墙啊！",
               "喂喂喂！你爪子带电啊？（偷偷往回挪半寸）",
               "坏蛋！偷袭算什么本事……（脚尖悄悄勾住对方鞋带）",
               "吵死了，再唠叨就用糖堵你嘴！",
               "啧，靠这么近想偷我笔记吗？",
               "哈卡奈",
               "修哇修哇",
               "一自摸多力",
               "msk是msk，米歇尔是米歇尔！",
               "小心爱美",
               "Happy,lucky,smile,yeah!!!",
               "噜~",
               "我只有吉他了",
               "頂点へ 狂い咲け!",
               "做了！",
               "a ↗ ri ↗↘sa↗ ，↗o↘ta↘↗e",
               "什么!",
               "全体出动，（）！",
               "说，你是猪！",
               "武士道",
               "ふええええええ",
               "丸之山上缤纷彩",
               "KiraKiradokidoki",
               " 你有为Roselia献上一切的觉悟吗！",
               " 你有为Poppin'Party献上一切的觉悟吗！",
               "其实米歇尔设定上有个妹妹...",
               "大e长 35w q1",
               "大家我都喜欢哦",
               "道德上有问题\n终于欲望吧",
               "ki拉ki拉hi卡撸～",
               "跟我组一辈子乐队吗",
               "秋妈妈～",
               "为什么要演春日影！！！",
               "我小时候，听见过星星的声音",
               "偶内盖，saki酱一耐多，哇达西",
               "主唱是星星",
               "火速展示吧"
        ]

# 配置参数（可在.env文件中覆盖）
class PokeConfig:
    # 基础冷却时间（秒）
    COOLDOWN_TIME: int = 10

    # 连戳惩罚系数（每连续戳一次增加多少秒冷却）
    PUNISH_FACTOR: float = 2

    # 最大冷却时间（秒）
    MAX_COOLDOWN: int = 60

    # 响应消息模板
    RESPONSE_MSG: list = msg

    # 冷却提示消息
    COOLDOWN_MSG: str = "⌛ 您戳得太快了，请等待 {remaining} 秒后再试~"

    # 特殊用户白名单（不受冷却限制）
    VIP_USERS: set = {1122}

    # 是否启用反戳功能
    ENABLE_POKE_BACK: bool = True


# 创建戳一戳事件响应器
poke_matcher = on_notice(priority=9, block=True)


def get_cooldown_time(user_id: int) -> Tuple[float, bool]:
    """计算用户的剩余冷却时间"""
    now = datetime.now()

    # 白名单用户无冷却
    if user_id in PokeConfig.VIP_USERS:
        return 0.0, True

    # 获取上次响应时间
    last_time = cooldown_records.get(user_id)

    # 如果是第一次戳或已过冷却
    if last_time is None:
        return 0.0, True

    # 计算冷却剩余时间
    elapsed = (now - last_time).total_seconds()
    base_cooldown = PokeConfig.COOLDOWN_TIME

    # 计算连续惩罚 - 连续戳得越快，惩罚越大
    if elapsed < base_cooldown:
        # 连续惩罚 = 基础冷却 + 惩罚系数 * (基础冷却 - 已过时间)
        penalty = PokeConfig.PUNISH_FACTOR * (base_cooldown - elapsed)
        required_cooldown = min(base_cooldown + penalty, PokeConfig.MAX_COOLDOWN)
        remaining = max(0, required_cooldown - elapsed)
        return remaining, False

    return 0.0, True


@poke_matcher.handle()
async def handle_poke(event: PokeNotifyEvent):
    if event.group_id in plugin_config.ignored_groups:
        return
    # 调试日志
    logger.debug(f"收到戳一戳事件: {event.json()}")

    # 确保只响应戳机器人事件
    target_id = getattr(event, 'target_id', None)
    self_id = getattr(event, 'self_id', None) or bot_self_id

    if not target_id or not self_id or target_id != self_id:
        return

    user_id = event.user_id
    now = datetime.now()

    # 计算冷却状态
    remaining, is_ready = get_cooldown_time(user_id)

    # 如果在冷却中
    if not is_ready:
        # 发送冷却提示
        msg = PokeConfig.COOLDOWN_MSG.format(remaining=f"{remaining:.1f}")
        await poke_matcher.finish(MessageSegment.text(msg))

    # 更新冷却记录
    cooldown_records[user_id] = now

    # 构建响应消息
    response = random.choice(PokeConfig.RESPONSE_MSG)

    # 添加个性化回复
    if user_id in PokeConfig.VIP_USERS:
        response = MessageSegment.text("🌟 主人别戳了~") + MessageSegment.face(66)  # 害羞表情

    # 发送响应
    if response == " 你有为Roselia献上一切的觉悟吗！" or response == " 你有为Poppin'Party献上一切的觉悟吗！":
        await poke_matcher.finish(MessageSegment.at(event.user_id) +
                                  MessageSegment.text(response)
                                  )
    else:
        await poke_matcher.finish(response)


# 定时清理过期的冷却记录
async def clean_cooldown_records():
    """定期清理冷却记录"""
    while True:
        await asyncio.sleep(300)  # 每5分钟清理一次

        now = datetime.now()
        expired_users = []

        for user_id, last_time in cooldown_records.items():
            # 如果超过最大冷却时间2倍，清除记录
            if (now - last_time).total_seconds() > PokeConfig.MAX_COOLDOWN * 2:
                expired_users.append(user_id)

        for user_id in expired_users:
            del cooldown_records[user_id]
            logger.debug(f"清理用户冷却记录: {user_id}")
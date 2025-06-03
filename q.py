import time
import random


def dragon_boat_wishes(name="朋友"):
    # 端午节祝福语句库
    wishes = [
        f"✨{name}，端午节到啦！愿你像龙舟一样勇往直前，生活如粽子般香甜饱满～",
        f"🌿{name}端午安康！愿粽叶裹住所有好运，糯米粘满幸福时光，香囊装满平安喜乐～",
        f"🛶{name}，祝你端午假期：龙舟划出好心情，粽子吃出好运气，艾草带来好福气！",
        f"🍙端午至，祝福到～{name}，愿你生活‘粽’有甜蜜，日子‘粽’有如意，幸福‘粽’不缺席！",
        f"🌺{name}，送你一颗快乐粽：第一层是祝福，第二层是平安，第三层是健康，层层包裹你的美好时光～"
    ]

    # 动态输出祝福
    print("正在为你生成端午节祝福...\n")
    for i in range(3, 0, -1):
        print(f"加载中 {i}...")
        time.sleep(0.5)

    # 随机选择一条祝福
    wish = random.choice(wishes)

    # 彩色字符效果（终端支持时显示）
    color_codes = ["\033[31m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
    colored_wish = ""
    for i, char in enumerate(wish):
        color = color_codes[i % len(color_codes)]
        colored_wish += f"{color}{char}"

    # 结尾重置颜色
    colored_wish += "\033[0m"

    print("\n" + "=" * 50)
    print(colored_wish)
    print("=" * 50 + "\n")

    # 彩蛋：粽子表情动画
    print("送你一颗会跳舞的粽子～")
    for _ in range(3):
        print("  🎵 🍙💃🍙💃🍙 💫  ")
        time.sleep(0.5)
        print("  🌿 🍙✨🍙✨🍙 🎶  ")
        time.sleep(0.5)

# 调用函数，可自定义名字（比如改成你的朋友名字）
dragon_boat_wishes("亲爱的小伙伴")
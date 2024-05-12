import json
import requests


class Items:
    def __init__(self, name, gun_type, level, tradable, next_trade_time):
        self.name = name  # 市场名称
        self.type = gun_type  # 枪械种类
        self.level = level  # 品质
        self.tradable = tradable  # 是否可交易
        self.next_trade_time = next_trade_time  # 下次交易时间

    def serialized_print(self):
        trade_cn = "可交易" if self.tradable else "交易冷却中： " + self.next_trade_time

        print(f"""
            ---------------------------------
            {self.name}
            {self.type}  - {self.level}
            {trade_cn}   
            ---------------------------------
        """)


def judge_want(name, want_gun):
    flag = False
    for gun_name in want_gun:
        if name.startswith(gun_name):
            flag = True
            break
    return flag


def get_items(count: int, game_id: int):
    base_url = (f"https://steamcommunity.com/inventory/76561198364650650/"
                f"{str(game_id)}/2?l=schinese&count={str(count)}")
    # base_url = "https://steamcommunity.com/inventory/76561198364650650/730/2?l=schinese&count=75"
    print(base_url)
    res = requests.get(base_url,
                       headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                                'Pragma': 'no-cache',
                                'Cache-Control': 'no-cache',
                                })

    # 不带授权信息是没法看到枪的（交易冷却中的）
    json_res = json.loads(res.text)

    return json_res


if __name__ == "__main__":
    resp = get_items(75, 730)
    from pprint import pprint

    want_list = ["隐秘", "非凡", "保密", "受限"]
    want_gun = ["AK-47", "沙漠之鹰", "AWP"]

    descriptions = resp.get("descriptions")

    item_list = []
    if descriptions:
        for desc in descriptions:
            owner_info = desc.get("owner_descriptions", "None")
            tradable = desc.get("tradable", "0")
            name = desc.get("name", "未获取到枪械名称")
            market_name = desc.get("market_name", "未获取到枪械名称")
            type_info = desc.get("type", "")

            if type_info:
                type_list = type_info.split(' ')
                if len(type_list) > 2:
                    level, gun_type = type_info[1], type_list[2]
                else:
                    level, gun_type = type_list[0], type_list[1]
            else:
                continue

            try:
                next_trade_time = "随时可交易" if tradable else "".join("".join(x.get("value", "") for x in owner_info))
            except:
                continue  # 过滤徽章之类的

            # 只关注有价值的饰品
            if level in want_list and judge_want(name, want_gun):
                item = Items(name, gun_type, level, tradable, next_trade_time)
                item_list.append(item)

    if len(item_list) > 0:
        for item in item_list:
            item.serialized_print()
    else:
        print("饰品还在冷却中...")

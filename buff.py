import requests
import json
import os

cookies = os.getenv("Cookie")

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'Cookie': cookies,
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params1 = {
    'game': 'csgo',
    'force': '0',
    'page_num': '1',
    'page_size': '50',
    'search': '',
    'state': 'all',
    'rarity': 'ancient_weapon',
    '_': '1715748102081',
}

params2 = {
    'game': 'csgo',
    'force': '0',
    'page_num': '1',
    'page_size': '50',
    'search': '',
    'state': 'all',
    'rarity': 'legendary_weapon',
    '_': '1715748102081',
}

line_list = []


def crawler_buff(params_in):
    # 我没有steam开放商密钥，但是Buff有啊hhh
    response = requests.get('https://buff.163.com/api/market/steam_inventory', params=params_in, headers=headers)

    if response.text.find("<title>登录</title>") > 0:
        # 说明Cookie失效了 --- 发送更新Cookie的邮件（10天更新一次）
        with open("res.html", 'w') as file:
            file.write("Cookie过期,请手动更新secrets的Cookie")
    else:
        json_resp = json.loads(response.text)
        res_list = json_resp["data"]["items"]

        for item in res_list:
            tradable_text = item.get("tradable_text", "可交易")
            name = item.get("name", "商品名获取失败")
            icon_url = item.get("icon_url", "图片链接获取失败")

            line = f"""
                <img style="width: 100px ; height: 100px" src="{icon_url}">
                <div style="font-weight: bolder;color: red">{name}</div>
                <div>{tradable_text}</div>
            """
            line_list.append(line)

        line_list.insert(0, "<!DOCTYPE html><html lang=''><head><meta charset='utf-8'></head><body>")
        line_list.append("</body></html>")


if __name__ == "__main__":
    crawler_buff(params1)
    crawler_buff(params2)

    with open("res.html", 'a') as file:
        file.writelines(line_list)

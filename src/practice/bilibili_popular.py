import httpx

"""
    bilibili 综合热门
"""


# 过滤掉不要的分类
def not_care(elm: dict) -> bool:
    return elm["tname"] == "手机游戏"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
with httpx.Client(http2=True, headers=headers) as client:
    resp0 = client.get(
        "https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1&web_location=333.934&w_rid=0bb66a49c507b85753169e95a9facefb&wts=1733309552"
    )
    popular_list = resp0.json()["data"]["list"]

    # print(popular_list[0])

    for elm in popular_list:
        if not_care(elm):
            continue

        print(
            f"标题：{elm['title']}    作者：{elm['owner']['name']}    分类：{elm['tname']}    浏览量：{elm['stat']['view']}   标签：{elm['rcmd_reason']['content']}"  # AI：{elm['ai_rcmd']}
        )
        print()

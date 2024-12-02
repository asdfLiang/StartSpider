import urllib.robotparser

"""
    robots协议分析
"""

rp = urllib.robotparser.RobotFileParser(url="https://www.baidu.com/robots.txt")
rp.read()

# 判断网页是否可以抓取
print(rp.can_fetch("Baiduspider", "https://www.baidu.com"))
# 百度的robots.txt中没有限制Baiduspider对homepage页面的抓取
print(rp.can_fetch("Baiduspider", "https://www.baidu.com/homepage/"))
# 百度的robots.txt中限制了Googlebot对homepage页面的抓取
print(rp.can_fetch("Googlebot", "https://www.baidu.com/homepage/"))

"""
    Robots.txt 样例

    # 所有爬虫只能爬取public目录
    User-agent: *
    Disallow: /
    Allow: /public/

    # 对百度爬虫有效
    #   常见爬虫名称：
    #   Baiduspider     百度
    #   Googlebot       谷歌
    #   360Spider       360搜索
    #   YodaoBot        有道
    #   ia_archiver     Alexa
    #   Scooter         altavista
    #   Bingbot         必应
    User-agent: Baiduspider

    # 禁止所有爬虫访问所有目录
    User-agent: *
    Disallow: /

    # 允许所有爬虫访问所有目录
    User-agent: *
    Disallow:

    # 禁止所有爬虫访问某些目录：
    User-agent: *
    Disallow: /private/
    Disallow: /tmp/

    # 只允许某一个爬虫访问所有目录的代码：
    User-agent: WebCrawler
    Disallow:
    User-agent: *
    Disallow: /
"""

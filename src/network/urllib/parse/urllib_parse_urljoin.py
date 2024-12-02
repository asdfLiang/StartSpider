from urllib.parse import urljoin

"""
    链接合并
"""
print(urljoin("https://www.baidu.com", "FAQ.html"))
print(urljoin("https://www.baidu.com", "https://cuiqingcai.com/FAQ.html"))
print(urljoin("https://www.baidu.com/about.html", "https://cuiqingcai.com/FAQ.html"))
print(
    urljoin(
        "https://www.baidu.com/about.html", "https://cuiqingcai.com/FAQ.html?question=2"
    )
)
print(urljoin("https://www.baidu.com?wd=abc", "https://cuiqingcai.com/index.php"))
print(urljoin("https://www.baidu.com", "?category=2#comment"))
print(urljoin("www.baidu.com", "?category=2#comment"))
print(urljoin("www.baidu.com#comment", "?category=2"))

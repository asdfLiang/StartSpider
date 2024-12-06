from pyquery import PyQuery as pq
import requests

"""
    初始化链接
"""

doc = pq(url="https://cuiqingcai.com")
print(doc("title"))

doc = pq(requests.get("https://cuiqingcai.com").text)
print(doc("title"))

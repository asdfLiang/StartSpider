from pyquery import PyQuery as pq

"""
    初始化文件
"""

doc = pq(filename="tests/downloads/prettify.html")
print(doc)

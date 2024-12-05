from bs4 import BeautifulSoup

"""
    获取子节点及子孙节点
"""

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class = "title" name="dormouse"><b>The Dormouse's story</b></p>
<p class = "story">Once upon a time there were three little sisters; and their names were
<a href = "http://example.com/elsie" class = "sister" id = "link1"><!--Elsie--></a>,
<a href = "http://example.com/lacie" class = "sister" id = "link2">Lacie</a> and
<a href = "http://example.com/tillie" class="sister" id = "link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, "lxml")

# 直接子节点，结果是列表
print("Contents: ")
print(soup.p.contents)  # [<b>The Dormouse's story</b>]
print()

# 直接子节点，结果是迭代器
print("Childern: ")
print(soup.p.children)  # <list_iterator object at 0x00000280798B90F0>
for i, child in enumerate(soup.p.children):
    print(i, child)
print()

# 所有子孙节点
print("Desendants")
for i, child in enumerate(soup.p.descendants):
    print(i, child)
print()

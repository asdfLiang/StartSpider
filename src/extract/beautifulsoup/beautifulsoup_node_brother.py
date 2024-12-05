from bs4 import BeautifulSoup

"""
    获取兄弟节点
"""

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, "lxml")

print("最近兄弟节点：")
print("Next sibling: ", soup.a.next_sibling)  # 上一个兄弟节点
print("Prev sibling: ", soup.a.previous_sibling)  # 下一个兄弟节点
print()

print("所有兄弟节点：")
# 之后的所有兄弟节点
print("Next siblings: ", list(enumerate(soup.a.next_siblings)))
# 之前的所有兄弟节点
print("Prev siblings: ", list(enumerate(soup.a.previous_siblings)))
print()

from bs4 import BeautifulSoup

"""
    获取父节点及祖先节点
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

# 父节点
print("Parent: ")
print(soup.a.parent)
print()

# 所有祖先节点
print("Parents: ")
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))
print()

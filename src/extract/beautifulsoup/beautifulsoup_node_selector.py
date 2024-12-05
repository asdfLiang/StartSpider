from bs4 import BeautifulSoup

"""
    使用lxml解析器
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

# 输出标签<p>的文本内容
soup = BeautifulSoup("<p>Hello</p>", "lxml")
print(soup.p.string)

soup = BeautifulSoup(html, "lxml")
# 节点选择器
print(soup.title)  # <title>The Dormouse's story</title>
print(type(soup.title))  # <class 'bs4.element.Tag'>
print(soup.title)  # The Dormouse's story
print(soup.head)  # <head><title>The Dormouse's story</title></head>
print(soup.p)  # <p class="title" name="dormouse"><b>The Dormouse' story</b></p>

# 获取名称
print(soup.title.name)  # title 节点名称
print()

# 获取属性
print(soup.p.attrs)  # {'class': ['title'], 'name': 'dormouse'} 获取所有属性
print(soup.p.attrs["name"])  # dormouse 属性值
print()

# 获取内容
print(soup.p.string)  # The Dormouse' story
print()

# 嵌套选择
print(soup.head.title)  # <title>The Dormouse's story</title>
print(type(soup.head.title))  # <class 'bs4.element.Tag'>
print(soup.head.title.string)  # The Dormouse's story
print()

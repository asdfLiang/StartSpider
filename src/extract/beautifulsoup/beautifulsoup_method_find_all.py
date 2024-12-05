from bs4 import BeautifulSoup
import re

"""
    查询所有符合条件的元素

    基本语法：find_all(name, attrs, recursive, text, **kwargs)
"""

html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
    <div>
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
"""

soup = BeautifulSoup(html, "lxml")
# name 根据节点名查询
print("=========================== name ===========================")
print(soup.find_all(name="ul"))
print()
print(type(soup.find_all(name="ul")[0]))
print()
for ul in soup.find_all(name="ul"):
    print(ul.find_all(name="li"))
    for li in ul.find_all(name="li"):
        print(li, li.string)
print()

# attrs 根据节点属性查询
print("=========================== attrs ===========================")
print(soup.find_all(id="list-1"))
print()
print(soup.find_all(class_="element"))
print()

# text 根据节点文本查询
print("=========================== text ===========================")
print(soup.find_all(text=re.compile("link")))
print()

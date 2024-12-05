from bs4 import BeautifulSoup

"""
    CSS选择器
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
# 基本选择器
print(soup.select(".panel-heading"))  # 类选择
print()
print(soup.select("ul li"))  # 标签选择
print()
print(soup.select("#list-2 .element"))  # id选择
print()
print(type(soup.select("ul")[0]))
print()


# 嵌套选择
print("=========================== 嵌套选择 ===========================")
for ul in soup.select("ul"):
    print(ul.select("li"))
print()

print("=========================== 获取属性 ===========================")
for ul in soup.select("ul"):
    print(ul["id"])
    print(ul.attrs["id"])
print()

print("=========================== 获取文本 ===========================")
for li in soup.select("li"):
    print("Get Text: ", li.get_text())
    print("String: ", li.string)
print()

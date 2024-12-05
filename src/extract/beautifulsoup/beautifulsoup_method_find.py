from bs4 import BeautifulSoup

"""
    查询第一个匹配的元素
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
print(soup.find(name="ul"))
print()
print(type(soup.find(name="ul")))
print()
print(soup.find(class_="list"))
print()
print(soup.find(id="list-1"))
print()

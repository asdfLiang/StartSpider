from pyquery import PyQuery as pq

"""
    获取文本
"""

html = """
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
"""

doc = pq(html)

# 获取文本
a = doc(".item-0.active a")
print(a)
print(a.text())  # 忽略节点内部包含的所有html，只返回纯文字内容
print()

# 获取内部的HTML文本
li = doc(".item-0.active")
print(li)
print(li.html())
print()

# 获取文本 - 选中多节点，注意text会将多个节点的内容拼接后返回
li = doc("li")
print(li.html())  # first item
print(li.text())  # first item second item third item fourth item fifth item
print(type(li.text()))

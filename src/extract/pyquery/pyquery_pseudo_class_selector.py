from pyquery import PyQuery as pq

"""
    伪类选择器
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
li = doc("li:first-child")  # 第一个li节点
print(li)
print()
li = doc("li:last-child")  # 最后一个li节点
print(li)
print()
li = doc("li:nth-child(2)")  # 第二个li节点
print(li)
print()
li = doc("li:gt(2)")  # 第三个li之后的节点
print(li)
print()
li = doc("li:nth-child(2n)")  # 偶数位置的li节点
print(li)
print()
li = doc("li:contains(second)")  # 包含second文本的li节点
print(li)

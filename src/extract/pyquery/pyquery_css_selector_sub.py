from pyquery import PyQuery as pq

"""
    查找子节点
"""

html = """
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""

# 查找class="list"的节点
doc = pq(html)
items = doc(".list")
print(type(items))
print(items)
print()

# 查找所有子孙节点
lis = items.find("li")
print(type(lis))
print(lis)
print()

# 查找所有子节点
lis = items.children()
print(type(lis))
print(lis)
print()

# 查找class="active"的子节点
lis = items.children(".active")
print(type(lis))
print(lis)
print()

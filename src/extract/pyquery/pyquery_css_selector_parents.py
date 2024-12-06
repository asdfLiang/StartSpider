from pyquery import PyQuery as pq

"""
    查找父节点
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

# 查找父节点
doc = pq(html)
items = doc(".list")
container = items.parent()
print(type(container))
print(container)
print()

# 查找祖先节点
parents = items.parents()
print(type(parents))
print(parents)
print()

# 查找某个祖先节点
parent = items.parents(".wrap")
print(parent)
print()

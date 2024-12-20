from pyquery import PyQuery as pq

"""
    节点修改class
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

# 删除class
li = doc(".item-0.active")
print(li)
print("================================================")
li.remove_class("active")
print(li)
print("================================================")
# 添加class
li.add_class("active")
print(li)

from pyquery import PyQuery as pq

"""
    节点内容操作（attr、text、html）
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

li = doc(".item-0.active")
print(li)
li.attr("name", "link")  # 添加属性
print(li)
li.text("changed item")  # 修改文本
print(li)
li.html("<span>changed item</span>")  # 修改html文本
print(li)

from parsel import Selector

"""
    初始化
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

# css方法提取节点
selector = Selector(text=html)
items = selector.css(".item-0")
print(len(items))
print(type(items))
print(items)
print()
for item in items:
    print(item)

# xpath方法提取节点
print("=====================================================")
items2 = selector.xpath("//li[contains(@class, 'item-0')]")
print(len(items2))
print(type(items2))
print(items2)
print()
for item in items2:
    print(item)

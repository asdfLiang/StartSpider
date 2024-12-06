from parsel import Selector

"""
    提取文本
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

# 使用css方式获取结果
selector = Selector(text=html)
items = selector.css(".item-0")
for item in items:
    text = item.xpath(".//text()").get()
    print(text)
print()

# 获取第一个Selector对象的结果
result = selector.xpath("//li[contains(@class, 'item-0')]//text()").get()
print(result)
print()

# 获取所有Selector对象的结果
result = selector.xpath("//li[contains(@class, 'item-0')]//text()").getall()
print(result)
print()

# 使用css方式获取相同结果 *提取所有子节点 ::text提取文本
result = selector.css(".item-0 *::text").getall()
print(result)
print()

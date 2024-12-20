from parsel import Selector

"""
    正则提取
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

selector = Selector(text=html)

# 匹配class="item-0"下所有包含link的的结果
result = selector.css(".item-0").re("link.*")
print(result)
print()

# 只针对文本提取
result = selector.css(".item-0 *::text").re(".*item")
print(result)
print()

# 提取第一个符合规则的结果
result = selector.css(".item-0").re_first('<span class="bold">(.*?)</span>')
print(result)
result = selector.css(".item-0").re_first("<span class='bold'>(.*?)</span>")
print(result)

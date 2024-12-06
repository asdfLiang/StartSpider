from pyquery import PyQuery as pq

"""
    获取属性
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

# 获取单个节点
li = doc(".item-0.active")
print(li)
print(str(li))
print()

# 遍历节点
lis = doc("li").items()
print(type(lis))
for li in lis:
    print(li, type(li))
print()

# 获取属性
a = doc(".item-0.active a")
print(a, type(a))
print(a.attr("href"))
print(a.attr.href)
print()

# 获取属性 - 选取多个元素
a = doc("a")
print(a, type(a))
print(a.attr("href"))  # 只会输出第一个
print(a.attr.href)  # 只会输出第一个
print()

# 获取属性 - 获取所有a节点的属性
for item in a.items():
    print(item.attr.href)
print()

from pyquery import PyQuery as pq

"""
    节点删除
"""

html = """
<div class="wrap">
    Hello, World
    <p>This is paragraph</p>
</div>
"""

doc = pq(html)

wrap = doc(".wrap")
print(wrap.text())
print()
# 目标是提取Hello, World，删除p节点
wrap.find("p").remove()
print(wrap.text())

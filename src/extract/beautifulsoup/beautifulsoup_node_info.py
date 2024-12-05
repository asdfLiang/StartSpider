from bs4 import BeautifulSoup

"""
    提取信息
"""

html = """
<html>
    <body>
        <p class = "story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</b>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        </p>
"""

soup = BeautifulSoup(html, "lxml")
print("Next sibling:")
print(type(soup.p.next_sibling))  # <class 'bs4.element.NavigableString'>
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print()

print("Prev sibling:")
print(type(soup.a.parents))
print(soup.a.next_sibling)
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs["class"])

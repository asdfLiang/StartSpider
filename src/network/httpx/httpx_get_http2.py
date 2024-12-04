import httpx

"""
    http2请求
"""

client = httpx.Client(http2=True)
resp2 = client.get("https://spa16.scrape.center/")
print(resp2.text)

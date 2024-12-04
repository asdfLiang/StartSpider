import requests
from requests.auth import HTTPBasicAuth

"""
    身份认证
"""

resp0 = requests.get(
    "https://ssr3.scrape.center/", auth=HTTPBasicAuth("admin", "admin")
)
print(resp0.status_code)

# 简写
resp1 = requests.get("https://ssr3.scrape.center/", auth=("admin", "admin"))
print(resp1.status_code)

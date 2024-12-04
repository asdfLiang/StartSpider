import requests
from requests.packages import urllib3
import logging

# https报错
resp0 = requests.get("https://ssr2.scrape.center/", verify=False)
print(resp0.status_code)

# 通过logging捕获告警到日志
logging.captureWarnings(True)
resp1 = requests.get("https://ssr2.scrape.center", verify=False)
print(resp1.status_code)

# 指定一个本地证书用作客户端证书，必须有本地证书
# resp2 = requests.get(
#     "https://ssr2.scrape.center", cert=("/path/server.crt", "/path/server.key")
# )
# print(resp2.status_code)

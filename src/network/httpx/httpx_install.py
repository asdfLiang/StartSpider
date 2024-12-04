import requests

"""
    http2错误演示及安装
"""

resp = requests.get("https://spa16.scrape.center/", verify=True)
print(resp.status_code)

"""
    pip install httpx -i https://pypi.mirrors.ustc.edu.cn/simple/
    pip install "httpx[http2]" -i https://pypi.mirrors.ustc.edu.cn/simple/
"""

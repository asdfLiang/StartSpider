import requests

"""
    Session 维持
"""

withSession = requests.Session()
withSession.get("https://www.httpbin.org/cookies/set/number/123456789")
resp = withSession.get("https://www.httpbin.org/cookies")
print(resp.text)

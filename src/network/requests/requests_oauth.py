import requests
from requests_oauthlib import OAuth1

# 请求格式
url = "https://api.twitter.com/1.1/account/verify_credentials.json"
auth = OAuth1(
    "YOU_APP_KEY", "YOU_APP_SECRET", "USER_OAUTH_TOKEN", "USER_OAUTH_TOKEN_SECRET"
)
resp = requests.get(url=url, auth=auth)

import httpx
from free_proxy import proxy

"""    
    httpx 设置http代理（通过）
"""

with httpx.Client(proxy=f"http://{proxy}") as client:
    try:
        response = client.get("https://www.httpbin.org/get", timeout=10)
        print(response.text)
    except httpx.RequestError as e:
        print(f"An error occurred: {e}")
    except httpx.TimeoutException as e:
        print(f"Request timed out: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")

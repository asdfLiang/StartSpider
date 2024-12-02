from urllib.parse import parse_qs, parse_qsl

"""
    序列化反序列化
"""

# 序列化
query = "name=germey&age=25"
print(parse_qs(query))

# 反序列化
print(parse_qsl(query))

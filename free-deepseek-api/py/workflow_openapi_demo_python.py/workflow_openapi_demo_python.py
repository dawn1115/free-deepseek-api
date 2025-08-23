import http.client
import json
import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

# 获取用户手动输入
user_input = input("请输入要发送的内容: ")

headers = {
    "Content-Type": "application/json",
    "Accept": "text/event-stream",
    "Authorization": "Bearer 2563e7415939bf27e627edc78f2ce83a:YWY3OTU0MjI0NjM5NzRiMjUwMDI5MjNj",
}

data = {
    "flow_id": "7361279241469214722",
    "uid": "123",
    "parameters": {"AGENT_USER_INPUT": user_input},
    "ext": {"bot_id": "adjfidjf", "caller": "workflow"},
    "stream": False,
}
payload = json.dumps(data)

conn = http.client.HTTPSConnection("xingchen-api.xf-yun.com", timeout=120)
conn.request(
    "POST", "/workflow/v1/chat/completions", payload, headers, encode_chunked=True
)
res = conn.getresponse()

if data.get("stream"):
    while chunk := res.readline():
        print(chunk.decode("utf-8"))
else:
    data = res.readline()
    print(data.decode("utf-8"))

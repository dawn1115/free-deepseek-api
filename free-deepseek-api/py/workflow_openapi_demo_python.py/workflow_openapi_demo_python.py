import http.client
import json
import ssl
import socket
import uuid

# ssl._create_default_https_context = ssl._create_unverified_context

# 获取用户手动输入
user_input = input("请输入要发送的内容: ")

# 获取MAC地址和IP地址
def get_mac_address():
    try:
        # 获取第一个网络接口的MAC地址
        mac = uuid.getnode()
        mac_str = ':'.join(['{:02x}'.format((mac >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
        return mac_str
    except:
        return "unknown_mac"

def get_ip_address():
    try:
        # 获取本机IP地址
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        return "unknown_ip"

# 生成包含MAC和IP的uid
mac_address = get_mac_address()
ip_address = get_ip_address()
uid = f"{mac_address}_{ip_address}"

headers = {
    "Content-Type": "application/json",
    "Accept": "text/event-stream",
    "Authorization": "Bearer 2563e7415939bf27e627edc78f2ce83a:YWY3OTU0MjI0NjM5NzRiMjUwMDI5MjNj",
}

data = {
    "flow_id": "7361279241469214722",
    "uid": uid,
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
    response_data = res.readline().decode("utf-8")
    try:
        # 尝试解析JSON响应
        json_data = json.loads(response_data)
        # 提取并显示关键信息
        if json_data.get("code") == 0:
            content = json_data.get("choices", [{}])[0].get("delta", {}).get("content", "")
            print("回复内容：", content)
            # 显示token使用情况
            usage = json_data.get("usage", {})
            print(f"使用token：提示词{usage.get('prompt_tokens', 0)}，回复{usage.get('completion_tokens', 0)}，总计{usage.get('total_tokens', 0)}")
        else:
            print(f"请求失败：{json_data.get('message', '未知错误')}")
    except json.JSONDecodeError:
        print("响应格式错误：", response_data)
    except Exception as e:
        print(f"处理响应时出错：{str(e)}")

# 获取不在规则中的域名列表
import websocket
import json
import time

# WebSocket 服务器地址
ws_url = "ws://192.168.0.1:9999/connections?token="

# 已记录的 hosts
recorded_hosts = set()
log_file = "hosts_log.txt"

# 将 host 写入文件
def log_host_to_file(host):
    with open(log_file, "a") as f:
        f.write(f"{host}\n")

def on_message(ws, message):
    data = json.loads(message)
    
    # 遍历每个连接，筛选 rule 为 "Match" 的 host
    for connection in data.get("connections", []):
        if connection.get("rule") == "Match":
            host = connection["metadata"].get("host", "")
            
            # 如果 host 未记录过，进行记录并写入文件
            if host and host not in recorded_hosts:
                print(f"记录 host: {host}")
                recorded_hosts.add(host)
                log_host_to_file(host)

def on_error(ws, error):
    print(f"WebSocket 错误: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket 连接关闭，5 秒后重连...")
    time.sleep(5)
    connect_websocket()

def on_open(ws):
    print("WebSocket 连接成功")

def connect_websocket():
    ws = websocket.WebSocketApp(
        ws_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()

# 启动 WebSocket 连接
connect_websocket()


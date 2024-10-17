#!/bin/bash

# 定义请求的URL和授权头
script_dir=$(dirname "$0")
log_file="$script_dir/logs/logfile.log"
url_to_check="https://chatgpt.com"
put_url="http://192.168.51.1:9090/proxies/%F0%9F%9A%80%20%E6%89%8B%E5%8A%A8%E5%88%87%E6%8D%A2"
authorization_header="Authorization: Bearer 123456"
proxy_names=("Japan | 01" "Singapore | 01" "Japan 01" "Singapore 01" "Japan | 02" "Japan | 03" "Singapore | 02" "Singapore | 03")

echo $log_file


# 函数：发送PUT请求
send_put_request() {
    local proxy_name="$1"
    local data="{\"name\":\"$proxy_name\"}"
    curl --noproxy "*" -s -H "$authorization_header" -X PUT -d "$data" "$put_url"
}

# 函数：检查URL
check_url() {
	    curl -s "$url_to_check" > /dev/null
    return $?
}

# 记录日志的函数
log() {
    local message="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" >> "$log_file"
}

# 主逻辑
# 尝试请求URL

if check_url; then
    echo "URL is reachable"
else
    echo "URL is not reachable, switching proxy"
    for proxy_name in "${proxy_names[@]}"; do
        send_put_request "$proxy_name"
        sleep 2  # 等待几秒钟以便代理切换生效

        # 再次尝试请求URL
        if check_url; then
             log "URL is reachable with proxy $proxy_name"
            exit 0
        fi
    done
fi

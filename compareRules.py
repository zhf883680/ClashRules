import requests

# 从URL读取文件内容
def get_file_content(url):
    response = requests.get(url)
    response.raise_for_status()  # 如果请求失败，抛出异常
    return set(response.text.splitlines())  # 按行分割内容并转换为集合

# 多组文件，每组包括一个基准文件和若干需要比对的文件
file_groups = [
    {
        'base_file_url': 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaDomain.list',  # 第一组基准文件
        'compare_file_url': 'https://raw.githubusercontent.com/LM-Firefly/Rules/refs/heads/master/Domestic.list',  # 第一组待比对文件
        'output_filename': 'otherChinaDomain.list'  # 第一组的输出文件名
    },
    {
        'base_file_url': 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaCompanyIp.list',  # 第二组基准文件
        'compare_file_url': 'https://raw.githubusercontent.com/LM-Firefly/Rules/refs/heads/master/CCC-CN.list',  # 第二组待比对文件
        'output_filename': 'otherChinaIp.list'  # 第二组的输出文件名
    },
    # 可以添加更多的组
]

# 对每组文件进行比对
for group_index, file_group in enumerate(file_groups, start=1):
    # 获取基准文件的内容
    base_file_content = get_file_content(file_group['base_file_url'])
    
    # 获取待比对文件的内容
    compare_file_content = get_file_content(file_group['compare_file_url'])

    # 找出基准文件比其他文件多的内容
    base_diff_compare = base_file_content - compare_file_content

    # 如果基准文件比对方多的内容存在，才输出到文件
    if base_diff_compare:
        # 使用每组指定的输出文件名
        output_filename = file_group['output_filename']

        # 输出结果到指定文件
        with open(output_filename, 'w', encoding='utf-8') as output_base_diff:
            output_base_diff.writelines("\n".join(base_diff_compare))
        
        print(f"组{group_index}的比对完成，结果已保存为：{output_filename}")
    else:
        print(f"组{group_index}与基准文件没有差异。")

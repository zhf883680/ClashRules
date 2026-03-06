#!/usr/bin/env python3
"""
将 rule-providers 目录下的 Clash 规则文件转换为 Loon 格式
- 去除 payload: 行
- 去除每行的 - 前缀
"""

import os
import shutil
from pathlib import Path


def convert_file(input_path: Path, output_path: Path) -> None:
    """转换单个文件"""
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    converted_lines = []
    for line in lines:
        line = line.rstrip('\n')
        # 跳过 payload: 行
        if line.strip() == 'payload:':
            continue
        # 去除 - 前缀 (包括后面的空格)
        if line.strip().startswith('- '):
            # 保留原始缩进（如果有的话）
            stripped = line.strip()
            converted_line = stripped[2:]  # 去除 "- "
            converted_lines.append(converted_line)
        elif line.strip():  # 非空行
            converted_lines.append(line)

    # 确保输出目录存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 写入转换后的文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(converted_lines))
        if converted_lines:
            f.write('\n')  # 文件末尾添加换行符

    print(f"✓ 已转换: {input_path.name} -> {output_path}")


def main():
    # 定义输入和输出目录
    base_dir = Path(__file__).parent
    input_dir = base_dir / 'rule-providers'
    output_dir = base_dir / 'rule-loon'

    # 检查输入目录是否存在
    if not input_dir.exists():
        print(f"错误: 输入目录 {input_dir} 不存在")
        return

    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)

    # 获取所有 yaml 文件
    yaml_files = list(input_dir.glob('*.yaml')) + list(input_dir.glob('*.yml'))

    if not yaml_files:
        print("没有找到 yaml 文件")
        return

    print(f"找到 {len(yaml_files)} 个文件待转换...\n")

    # 转换每个文件
    for input_file in sorted(yaml_files):
        output_file = output_dir / input_file.name
        try:
            convert_file(input_file, output_file)
        except Exception as e:
            print(f"✗ 转换失败 {input_file.name}: {e}")

    print(f"\n完成! 所有文件已转换到 {output_dir}")


if __name__ == '__main__':
    main()

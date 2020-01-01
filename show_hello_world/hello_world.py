#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time: 2020-01-01 15:43
# @Software: python
# @File: hello_world.py
# @Author: Peter Ren
# @Contact: cnprogrammer@126.com
# @Site: 
# @IDE: PyCharm


import argparse


def show_message(msg: str):
    print(msg)


if __name__ == '__main__':
    show_message('Hello, 2020!')

    args = argparse.ArgumentParser('输入参数')
    args.add_argument('-n', '--name', help='你的姓名', required=True, type=str)
    a = args.parse_args()
    name = a.name
    print(name)
    show_message(name)

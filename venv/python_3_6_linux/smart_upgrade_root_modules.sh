#!/usr/bin/env bash
#pip install --upgrade pip==19.1.1 -i https://mirrors.aliyun.com/pypi/simple #19.2 error
python3 update_all_modules.py "python3 -m pip " ${1} #https://mirrors.aliyun.com/pypi/simple

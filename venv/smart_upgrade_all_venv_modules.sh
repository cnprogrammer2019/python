#!/usr/bin/env bash
for file_name in `find .|grep activate$`
do
	echo '=========================================================='
	echo ${file_name}
	echo '=========================================================='
	source ${file_name}
#	python3 -m pip install pip==19.1.1 -i https://mirrors.aliyun.com/pypi/simple #19.2 error
	python3 update_all_modules.py pip3 ${1} # https://mirrors.aliyun.com/pypi/simple
	deactivate
	echo 
done

#!/bin/bash
#echo ${1}，环境名称，例如：python3_django
#echo ${2}，镜像服务器，例如：https://mirrors.aliyun.com/pypi/simple
#echo ${3}，希望的安装包，例如：numpy,pandas,seabor,django
#
activate_name="/bin/activate"
venv_name=${1}
mserver=${2}
#
python3 -m venv ${venv_name}
echo '=========================================================='
echo ${venv_name}
echo '=========================================================='
#echo ${1}${activate_name}
source ${1}${activate_name}
#echo ${2}
#pip3 install -i ${2} pip==19.1.1
#pip3 install -i ${2} setuptools==41.0.1

pip3 install pip --upgrade -i ${2}
modstring=${3}
pip3 install ${modstring} -i ${mserver}

deactivate
echo

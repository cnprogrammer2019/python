快速生成Linux下的python 3.6 (ubuntu 18.04 LTS)的环境

**单独安装**：
./install_python3_venv.sh "虚拟环境名称" "镜像服务器" "以空格隔离的安装模块列表"

例：
./install_python3_venv.sh pure https://mirrors.aliyun.com/pypi/simple "pep8 pyinstaller"
建立 pure目录，镜像使用阿里云，安装的包是pep3和pyinstaller

**自动安装**：
./easy_install.sh "镜像服务器"

./easy_install.sh 内容：
#!/usr/bin/env bash
./install_python3_venv.sh pure ${1} "pep8"
./install_python3_venv.sh django ${1} "django autopep8 pytest"

**升级**：
./smart_upgrade_all_venv_modules.sh "镜像服务器"
自动升级目录下的所有虚拟环境的所有需要升级的模块
需要注意的一点就是有些依赖版本的没有考虑

./smart_upgrade_root_modules.sh "镜像服务器"
升级系统的，先进入root环境

**模块**：
一些我认为有用的模块文件：modules.txt
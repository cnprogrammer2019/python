快速生成Windows下的python 3.7 (Windows 7, 32bit)的环境

**单独安装**：
easy_install_venv.bat "虚拟环境名称" "镜像服务器" "以空格隔离的安装模块列表"

例：
./easy_install_venv.bat pure https://mirrors.aliyun.com/pypi/simple "pep8 pyinstaller"
建立 pure目录，镜像使用阿里云，安装的包是pep3和pyinstaller

**自动安装**：
easy_install.bat "镜像服务器"

easy_install.bat 内容：
call easy_install_venv.bat pure %1 "pep8"
call easy_install_venv.bat finance %1 "numpy pandas pep8 autopep8 pytest"

**升级**：
upgrade_all_venv_modules.bat "镜像服务器"
自动升级目录下的所有虚拟环境的所有需要升级的模块
需要注意的一点就是有些依赖版本的没有考虑

update_all_modules.py "python -m pip " "镜像服务器"
升级系统的，需要系统管理员权限

**模块**：
一些我认为有用的模块文件：modules.txt
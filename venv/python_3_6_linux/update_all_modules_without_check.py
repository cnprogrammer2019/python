import subprocess
import sys

def update_all_modules_without_check(server, cmd='pip3'):
    '''
    最傻的办法，不检查是否需要升级（比较版本，所有的都走一遍
    :param server: 镜像服务器地址
    :param cmd: 使用的命令，默认pip3
    :return:
    '''
    com_list_o = cmd + ' list '
    if len(server) > 0:
        com_list_o = com_list_o + " -i " + server
    # 执行命令并返回结果
    # print(com_list_o)
    p = subprocess.Popen(com_list_o, shell=True, stdout=subprocess.PIPE)
    # 取命令返回结果，结果是一个二进制字符串，包含了我们上面执行pip list -o后展现的所有内容
    out = p.communicate()[0]
    # 二进制转utf-8字符串
    out = str(out, 'utf-8')

    # 切出待升级的包名, 并存入列表
    need_update = []
    for i in out.splitlines()[2:]:
        need_update.append(i.split(' ')[0])

    # 如果没有需要更新的就返回
    if len(need_update) == 0:
        print("no need to update")
        return

    # 执行升级命令，每次取一个包进行升级，pip只支持一个包一个包的升级
    for nu in need_update:
        com_update = cmd + ' install --upgrade {py}'.format(py=nu)
        if len(server) > 0:
            com_update = com_update + " -i " + server
        # print("执行命令:", com_update)
        subprocess.call(com_update, shell=True)
        # print("{com} is over\n".format(com=com_update))

if __name__ == "__main__":
    try:
        pip_cmd = sys.argv[1]
    except:
        pip_cmd = "pip"
    try:
        pip_mirror_server = sys.argv[2]
    except:
        pip_mirror_server = "https://mirrors.aliyun.com/pypi/simple"

    update_all_modules_without_check(cmd=pip_cmd, server=pip_mirror_server)

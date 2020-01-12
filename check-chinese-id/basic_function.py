#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time: 2020-01-12 12:18
# @Project: github-python
# @Author: Peter Ren
# @Email: cnprogrammer@126.com
# @Github: https://github.com/cnprogrammer2019
# @Site: http://www.peterren.net
# @File : basic_function.py
# @Software: PyCharm
"""
专为中华人民共和国居民身份证使用
"""


def check_id_18_validity(id):
    """
    检查18位身份证的验证码
    :param id: 18位身份证号码，字符串
    :return: 符合国标返回True
    """
    success = False
    try:
        id_len = len(id)
        if id_len == 15:
            return False
        if id_len != 18:
            return False
        weight_i = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        weight_len = len(weight_i)
        id_sum = 0
        for i in range(0, weight_len):
            id_sum = id_sum + int(id[i]) * weight_i[i]
        check_value = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
        check_value_index = id_sum % len(check_value)

        if str(id[id_len - 1]).upper() == check_value[check_value_index]:
            success = True
    except:
        pass

    return success


def calculate_id_18th_position(id):
    """
    返回18位身份证最后一位验证码
    :param id: 身份证前17位
    :return: 返回0-X值
    """
    suc = False
    check_result = ''
    try:
        id_len = len(id)
        if id_len == 17:
            weight_i = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            weight_len = len(weight_i)
            id_sum = 0
            for i in range(0, weight_len):
                id_sum = id_sum + int(id[i]) * weight_i[i]
            check_value = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
            check_value_index = id_sum % len(check_value)

            check_result = check_value[check_value_index]
            suc = True
    except:
        suc = False

    return suc, check_result


def trans_15_to_18(id_15, century='19'):
    """
    身份证升级，一代15位转18位
    :param id_15: 15位身份证号码
    :param century: 填充年，18XX=18， 19XX=19，原则上只有这两种可能
    :return: 成功与否，15位id，18位id
    """
    try:
        new_id_17 = id_15[0:6] + century + id_15[6:]
        suc, result = calculate_id_18th_position(new_id_17)
        new_id_18 = new_id_17 + result
        return suc, id_15, new_id_18
    except:
        return False, id_15, ""


def generate_id_18(area_code, year_code, month_code, day_code, sequence_code):
    """
    生成身份证18位
    :param area_code: 地区代码，6位数字组成的，但是最好是字符串
    :param year_code: 年代码，4位数字组成的，但是最好是字符串
    :param month_code: 月代码，2位数字组成的，但是最好是字符串
    :param day_code: 日代码，2位数字组成的，但是最好是字符串
    :param sequence_code: 顺序代码，3位数字组成的，但是最好是字符串，男=奇数，女=偶数，特殊的未处理（百岁老人）
    :return:
    """
    try:
        raw_code = str(area_code) + str(year_code) + str(month_code) + str(day_code) + str(sequence_code)
        suc, result = calculate_id_18th_position(raw_code)
        return suc, raw_code + result
    except:
        return False, ''


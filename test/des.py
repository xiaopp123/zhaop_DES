# -*- coding: utf-8 -*-
from utils import *


def code(text, key):
    output = ""
    turn_len = 0

    # 将密文和秘钥转换成二进制
    """先将文本转换成十六进制，然后将十六进制串转换成二进制"""

    hex_text = from_unicode_to_hex(text)
    # print(hex_text)
    binary_text = from_hex_to_binary(hex_text)

    hex_key = from_unicode_to_hex(key)
    binary_key = from_hex_to_binary(hex_key)

    # 如果秘钥长度不是16的整数倍则以增加0的方式变为16的整数倍
    # hex_text_len = len(hex_text)
    # hex_key_len = len(hex_key)

    turn_len = len(binary_text)
    binary_key_len = len(binary_key)

    # 对每64位进行一次加密
    for i in range(0, turn_len, 64):
        run_text = binary_text[i: i + 64]
        key_index = i % binary_key_len
        run_key = binary_key[key_index: key_index + 64]

        # 64位明文，秘钥初始化置换
        run_text = text_first_change(run_text)
        run_key = key_first_change(run_key)

        # print("run_text", run_text)
        # print(run_key)

        # 16次迭代
        for j in range(1):

            # 取出明文左右32位
            text_right = run_text[32:64]
            text_left = run_text[0:32]

            # 64左右交换
            run_text = text_right

            # 右边32位扩展置换
            text_right = extend_exchange(text_right)

            # 取本轮子密码
            key_left = run_key[0:28]
            key_right = run_key[28:56]

            # 根据轮数决定是左移一位或者两位
            key_left = key_left[d[j]:28] + key_left[0:d[j]]
            key_right = key_right[d[j]:28] + key_right[0:d[j]]

            run_key = key_left + key_right
            # print("run_key",run_key)

            # 对移动后的密码进行压缩置换(56->48)
            key_compress = key_second_change(run_key)

            # 子密码和明文右部分异或
            text_right = text_xor(text_right, key_compress)

            # S盒替换
            text_right = s_change(text_right)
            # print("text_right", text_right)

            # p转换
            text_right = p_change(text_right)

            # 异或
            text_right = text_xor(text_right, text_left)
            run_text += text_right

        # 32互换(是否需要)
        text_right = run_text[32:64]
        text_left = run_text[0:32]
        run_text = text_right + text_left

        # 将二进制转换位16进制，逆初始化置换
        output += ni_change(run_text)

    return output


# main
def des_encode(from_code, key):

    key_len = len(key)
    string_len = len(from_code)

    if string_len < 1 or key_len < 1:
        print("error input")
        return False

    key_code = code(from_code, key)

    return key_code


if __name__ == "__main__":
    print("des加密")
    # text = raw_input("请输入明文：")
    # key = raw_input("请输入秘钥：")

    # print(des_encode(text, key))
    u_str = '2014number中英文数字文转'
    code(u_str, u'1111')

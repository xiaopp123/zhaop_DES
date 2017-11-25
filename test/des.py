# -*- coding: utf-8 -*-
from utils import *


def code(text, key):
    output = ""
    turn_len = 0

    # 将密文和秘钥转换成二进制
    """先将文本转换成十六进制，然后将十六进制串转换成二进制"""

    hex_text = from_unicode_to_hex(text)
    print(hex_text)
    binary_text = from_hex_to_binary(hex_text)

    hex_key = from_unicode_to_hex(key)
    binary_key = from_hex_to_binary(hex_key)

    # 如果秘钥长度不是16的整数倍则以增加0的方式变为16的整数倍
    hex_text_len = len(hex_text)
    hex_key_len = len(hex_key)

    turn_len = len(binary_text)
    binary_key_len = len(binary_key)

    # 对每64位进行一次加密
    for i in range(0, turn_len, 64):
        run_text = binary_text[i:i+64]
        l = i % binary_key_len
        run_key = binary_key[l:l+64]

        # 64位明文，秘钥初始化置换
        run_text = text_first_change(run_text)
        run_key = key_first_change(run_key)




        # 16次迭代

            # 取出明文左右32位

            # 64左右交换

            # 右边32位扩展置换

            # 取本轮子密码

            # 子密码和明文右部分异或

            # S盒替换

            # p转换

            # 异或

        # 32互换

        # 将二进制转换位16进制，逆初始化置换
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

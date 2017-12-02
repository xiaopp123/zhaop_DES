# -*- coding: utf-8 -*-
from utils import *
from des_struct import *


def decode(text, key):

    output = ""

    text = text.encode("utf-8")

    # 将密文转换成二进制
    text_binary = from_hex_to_binary(text)

    # 获取子秘钥
    key = from_unicode_to_hex(key)
    key = get_key(key)
    key_len = len(key)
    # print(text_key)

    text_len = len(text_binary)
    #print(key)
    #print(key_len)

    # 对每64位进行一次加密
    for i in range(0, text_len, 64):
        run_text = text_binary[i:i + 64]
        run_key = key[i % key_len]

        # 64位明文初始置换
        run_text = text_first_change(run_text)

        # 16次迭代
        for j in range(16):
            text_right = run_text[32:64]
            text_left = run_text[0:32]

            # 64左右交换
            run_text = text_right

            # 右边32位扩展置换
            text_right = extend_exchange(text_right)

            # 获取本轮子秘钥
            key_y = run_key[15 - j]

            # 异或
            text_right = text_xor(text_right, key_y)

            # S盒
            text_right = s_change(text_right)

            # p转换
            text_right = p_change(text_right)

            # 异或
            text_right = text_xor(text_left, text_right)

            run_text += text_right

        # 32互换
        text_right = run_text[32:64]
        text_left = run_text[0:32]
        run_text = text_right + text_left

        # 将二进制转换成16进制，逆初始化
        output += ni_change(run_text)

    output = from_hex_to_unicode(output)
    return output


if __name__ == "__main__":
    text = raw_input("输入密文：")
    key = raw_input("请输入密码：")
    output = decode(text, key)
    #output = from_hex_to_unicode(output)
    print(output)

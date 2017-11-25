# -*- coding: utf-8 -*-


def code(self, from_code, key, code_len, key_len):
    output = ""
    turn_len = 0

    # 将密文和秘钥转换成二进制

    # 如果秘钥长度不是16的整数倍则以增加0的方式变为16的整数倍

    # 对每64位进行一次加密

        # 64位明文，秘钥初始化置换

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


# main
def des_encode(from_code, key):

    des = Des()
    key_len = len(key)
    string_len = len(from_code)

    if string_len < 1 or key_len < 1:
        print("error input")
        return False

    key_code = des.code(from_code, key, string_len, key_len)

    return key_code


if __name__ == "__main__":
    print("des加密")
    text = raw_input("请输入明文：")
    key = raw_input("请输入秘钥：")

    print(des_encode(text, key))

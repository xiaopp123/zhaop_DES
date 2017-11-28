# -*- coding: utf-8 -*-


def decode(text, key):

    # 将密文转换成二进制
    text_binary = from_hex_to_binary(text)

    # 获取子秘钥
    key = from_unicode_to_hex(key)
    text_key = get_key(key)





if __name__ == "__main__":
    decode("ccfc35ee8740ca295a94145b8209b44554294e3829ec65c5f40267d4054316c4", "1111")

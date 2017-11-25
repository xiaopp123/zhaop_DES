# -*- coding: utf-8 -*-
from des_struct import *


# from unicode to hexadecimal
def from_unicode_to_hex(text):
    hex_text = ""
    for i in text:
        hex_text += "%02x" % ord(i)

    return hex_text


# from hexadecimal to binary
def from_hex_to_binary(num):
    out_put = ""
    lens = len(num)
    lens = lens % 16
    for key in num:
        code_ord = int(key, 16)
        out_put += from_num_to_binary(code_ord, 4)
    if lens != 0:
        out_put += '0' * (16 - lens) * 4

    return out_put


# from a bit of hexadecimal to binary
def from_num_to_binary(key, lens):
    out_put = ""
    for i in range(lens):
        out_put = str(key >> i & 1) + out_put
    return out_put


# firt time to change text
def text_first_change(text):
    changed_text = ""
    for i in range(64):
        changed_text += text[ip[i] - 1]

    return changed_text


# first time to change key
def key_first_change(key):
    changed_key = ""
    for i in range(56):
        changed_key += key[pc1[i] - 1]

    return changed_key

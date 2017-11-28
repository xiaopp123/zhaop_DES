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


# from a num to binary
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


# second time to change key, from 56 to 48
def key_second_change(key):
    changed_key = ""
    for i in range(48):
        changed_key += key[pc2[i] - 1]

    return changed_key


# extend the right of the text from 32 to 48
def extend_exchange(text):
    extend_list = ""
    for i in range(48):
        extend_list += text[e[i] - 1]

    return extend_list


# operation of xor
def text_xor(text, key):
    text_len = len(text)
    out_put = ""
    for i in range(text_len):
        if text[i] == key[i]:
            out_put += '0'
        else:
            out_put += '1'

    return out_put


# s box change
def s_change(key):
    s_list = ""
    for i in range(8):
        row = int(str(key[i * 6]) + str(key[i * 6 + 5]), 2)
        col = ""
        for j in range(1, 5):
            col += str(key[i * 6 + j])
        col = int(col, 2)
        # make int to binary of 4 lengh
        s_list += from_num_to_binary(s[i][row][col], 4)

    return s_list

# p change
def p_change(text):
    p_list = ""
    for i in range(32):
        p_list += text[p[i] - 1]

    return p_list

# ni change
def ni_change(text):



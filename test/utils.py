# -*- coding: utf-8 -*-

def to_hex(text):
    hex_text = ""
    for i in text:
        hex_text += "%02x"%ord(i)

    return hex_text


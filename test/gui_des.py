# -*- coding: utf-8 -*-
from Tkinter import *


clas DesDesk():
    def __init__(self):
        window = Tk()
        window.title("des加密与解密")

        frame1 = Frame(window)
        frame1.pack()
        text_label = Label(frame1, text="请输入明文:")
        self.text = StringVar()
        text_entry = Entry(frame1, textvariable=self.text)

        key_label = Label(frame1, text="请输入密码:")
        self.key = StringVar()
        key_entry = Entry(frame1, textvariable=self.key)

        encode = Button(frame1, text="加密", )

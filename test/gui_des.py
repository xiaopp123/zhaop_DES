# -*- coding: utf-8 -*-
from Tkinter import *
import des
import des_1


class DesDesk():
    def __init__(self):
        window = Tk()
        window.title("des加密与解密")
        window.geometry('500x300+500+200')

       # frame1 = Frame(window)
       # frame1.pack()
        self.input_text = Text(window, height=5, width=50)
        self.input_text.place(x=60, y=10)

        key_label = Label(window, text="密码:")
        self.key = StringVar()
        key_entry = Entry(window, textvariable=self.key)
        key_entry['show'] = "*"

        key_label.place(x=60, y=100)
        key_entry.place(x=100, y=100)

        encode = Button(window, text="加密", command=self.encode_text)
        decode = Button(window, text="解密", command=self.decode_text)

        encode.place(x=300, y=100)
        decode.place(x=360, y=100)

        self.out_text = Text(window, height=5, width=50)
        self.out_text.place(x=60, y=150)

        #label = Label(window, text="解密").place(x=20,y=30)

       # text_area.grid(row=1, column=1)
       # text_entry.grid(row=1, column=2)

       # key_label.grid(row=2, column=1)
       # key_entry.grid(row=2, column=2)

       # encode.grid(row=2, column=1)

        window.mainloop()

    def encode_text(self):
        text = self.input_text.get("0.0", END).strip()
        key = self.key.get().strip()

        print("text:%s;key:%s" % (text, key))
        encoded_text = des.code(text, key)
        print("encode_text is %s" % encoded_text)

        # insert into out_put text
        self.out_text.insert(END, encoded_text)

    def decode_text(self):
        text = self.input_text.get("0.0", END).strip()
        key = self.key.get().strip()

        print("text:%s;key:%s" % (text, key))
        decoded_text = des_1.decode(text, key)
        print("decoded_text is %s" % decoded_text)

        self.out_text.insert(END, decoded_text)



DesDesk()




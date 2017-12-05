# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
from ScrolledText import ScrolledText
from PIL import ImageTk, Image
import des
import des_1


class DesDesk():
    def __init__(self):
        window = Tk()
        window.title("des加密与解密")
        window.geometry('500x300+500+200')
       # window['background'] = 'MintCream'
       # window['background'] = 'Moccasin'
       # window['background'] = 'Honeydew'
       # img_gif = PhotoImage(file='timg.gif')
       # image = Image.open(r'timg.gif')
       # background_image = ImageTk.PhotoImage(image)
       # background_image = ImageTk.PhotoImage(image)
       # window['background'] = background_image
       # window['background'] = img_gif
        window['background'] = "LightCyan"

       # window.iconbitmap("des.jpeg")

       # frame1 = Frame(window)
       # frame1.pack()

        font = "Times"
        font_color = "Wheat"
        input_label = Label(window, text="明文:")
        input_label.config(bg=font_color)
        input_label.config(font=font)
        input_label_y = 10
        input_label.place(x=60, y=input_label_y)

        self.input_text = Text(window, height=5, width=50)
        self.input_text.tag_config('a', foreground='red')
        self.input_text.place(x=60, y=input_label_y + 20)

        key_label = Label(window, text="密码:")
        key_label.config(font=font)
        key_label.config(bg=font_color)
        self.key = StringVar()
        key_entry = Entry(window, textvariable=self.key)
        key_entry['show'] = "*"
        key_label_y = 130

        key_label.place(x=60, y=key_label_y)
        key_entry.place(x=100, y=key_label_y)

        button_color = "LightCoral"
        encode = Button(window, text="加密", command=self.encode_text)
        encode.config(font=font)
        encode.config(bg=button_color)

        #decode_img = PhotoImage(file="decode.png")
        decode = Button(window, text="解密", command=self.decode_text)
        decode.config(font=font)
        decode.config(bg=button_color)

        encode.place(x=300, y=key_label_y)
        decode.place(x=360, y=key_label_y)

        out_label = Label(window, text="密文:")
        out_label.config(font=font)
        out_label.config(bg=font_color)
        out_label_y = 170
        out_label.place(x=60, y=out_label_y)
        self.out_text = Text(window, height=5, width=50)
        self.out_text.place(x=60, y=out_label_y + 20)

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

        if text == "" or text == None:
            print("请输入明文!")
            showinfo("提示", "请输入明文！")
            return

        if key == "" or key == None:
            print("请输入密码!")
            showinfo("提示", "请输入密码！")
            return

        print("text:%s;key:%s" % (text, key))
        encoded_text = des.code(text, key)
        print("encode_text is %s" % encoded_text)

        # clean out_put area
        self.out_text.delete("1.0", END)
        # insert into out_put text
        self.out_text.insert(END, encoded_text)

    def decode_text(self):
        text = self.out_text.get("0.0", END).strip()
        key = self.key.get().strip()

        if text == "" or text == None:
            print("请输入密文!")
            showinfo("提示", "请输入密文！")
            return

        if key == "" or text == None:
            print("请输入密码!")
            showinfo("提示", "请输入密码！")
            return

        print("text:%s;key:%s" % (text, key))
        try:
            decoded_text = des_1.decode(text, key)
            print("decoded_text is %s" % decoded_text)
        except Exception as e:
            showerror("", "解密过程出错请重试！")
            self.out_text.delete("1.0", END)
            self.key.set("")
            return

        self.input_text.delete("1.0", END)
        self.input_text.insert(END, decoded_text)


DesDesk()




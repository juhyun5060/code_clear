import tkinter
import tkinter.messagebox
import encoding

class encodeGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH = 800
        CANVAS_SIZE_HEIGHT = 500

        # root
        self.root = tkinter.Tk()
        self.root.title("ENCODING")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)

        # PhotoImage
        left_image = tkinter.PhotoImage(file="../image/SelectionEncode.png")
        label_img = tkinter.Label(self.root, image=left_image)
        label_img.pack(pady=40)

        # label(VIRTUAL KEY)
        label_key = tkinter.Label(self.root, text="VIRTUAL KEY", font=("roboto", "15"))
        label_key.place(x=190, y=220)

        # entry(virtual key)
        entry_key = tkinter.Entry(self.root, width=25, background="#ffffff", font=("roboto", "15"))
        entry_key.place(x=350, y=220)

        # label(PLAIN SENTENCE)
        label_sentence = tkinter.Label(self.root, text="PLAIN SENTENCE", font=("roboto", "15"))
        label_sentence.place(x=150, y=280)

        # entry(sentence)
        entry_sentence = tkinter.Entry(self.root, width=25, background="#ffffff", font=("roboto", "15"))
        entry_sentence.place(x=350, y=280)

        # button(GO)
        button_go = tkinter.Button(self.root, text="GO", width=10, foreground="#ffffff", font=("roboto", "15"),
                                      background="#000000",
                                      relief="flat", command=lambda: self.goClick(entry_key.get(), entry_sentence.get()))
        button_go.pack(side='bottom', pady=80)

        self.root.mainloop()

    def goClick(self, key, sentence):
        for k in key:
            if k in '~!@#$%^&*()_+`1234567890-=<>?,./':
                tkinter.messagebox.showinfo("오류", "특수문자는 입력 불가입니다.")
                self.root.destroy()
                encodeGUI()

        for s in sentence:
            if s in '~!@#$%^&*()_+`1234567890-=<>?,./':
                tkinter.messagebox.showinfo("오류", "특수문자는 입력 불가입니다.")
                self.root.destroy()
                encodeGUI()
        from GUI.result import ResultGUI
        self.root.destroy()
        encoding.encoding(key, sentence)
        ResultGUI()

if __name__ == '__main__':
    encodeGUI = encodeGUI()
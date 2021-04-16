import tkinter

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
        label_img = tkinter.Label(image=left_image)
        label_img.pack(pady=40)

        # label(VIRTUAL KEY)
        label_key = tkinter.Label(text="VIRTUAL KEY", font=("roboto", "15"))
        label_key.place(x=190, y=220)

        # entry(virtual key)
        entry_key = tkinter.Entry(self.root, width=25, background="#ffffff", font=("roboto", "15"))
        entry_key.place(x=350, y=220)

        # label(PLAIN SENTENCE)
        label_sentence = tkinter.Label(text="PLAIN SENTENCE", font=("roboto", "15"))
        label_sentence.place(x=150, y=280)

        # entry(sentence)
        entry_sentence = tkinter.Entry(self.root, width=25, background="#ffffff", font=("roboto", "15"))
        entry_sentence.place(x=350, y=280)

        # button(GO)
        button_go = tkinter.Button(self.root, text="GO", width=10, foreground="#ffffff", font=("roboto", "15"),
                                      background="#000000",
                                      relief="flat", command=lambda: self.goClick())
        button_go.pack(side='bottom', pady=80)

        self.root.mainloop()

    def goClick(self):
        self.root.destroy()
        # selectionGUI()

if __name__ == '__main__':
    decodeGUI = decodeGUI()
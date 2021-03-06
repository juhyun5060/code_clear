import tkinter
import sys
import os

class decodeGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH = 800
        CANVAS_SIZE_HEIGHT = 500

        # root
        self.root = tkinter.Tk()
        self.root.title("DECODING")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)

        # PhotoImage
        left_image = tkinter.PhotoImage(file="../image/SelectionDecode.png")
        label_img = tkinter.Label(self.root, image=left_image)
        label_img.pack(pady=40)

        # label(VIRTUAL KEY)
        label_key = tkinter.Label(self.root, text="VIRTUAL KEY", font=("roboto", "15"))
        label_key.place(x=180, y=220)

        # entry(virtual key)
        entry_key = tkinter.Entry(self.root, width=25, background="#ffffff", font=("roboto", "15"))
        entry_key.place(x=340, y=220)

        # label(SENTENCE)
        label_sentence = tkinter.Label(self.root, text="SENTENCE", font=("roboto", "15"))
        label_sentence.place(x=200, y=280)

        # entry(sentence)
        entry_sentence = tkinter.Entry(self.root, width=25, background="#ffffff", font=("roboto", "15"))
        entry_sentence.place(x=340, y=280)

        # button(GO)
        button_go = tkinter.Button(self.root, text="GO", width=10, foreground="#ffffff", font=("roboto", "15"),
                                      background="#000000",
                                      relief="flat", command=lambda: self.goClick())
        button_go.pack(side='bottom', pady=80)

        self.root.protocol('WM_DELETE_WINDOW', self.doSomething)

        self.root.mainloop()

    def goClick(self):
        self.root.destroy()
        # selectionGUI()

    def doSomething(self):
        sys.exit()

if __name__ == '__main__':
    decodeGUI = decodeGUI()
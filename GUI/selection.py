import tkinter
import encoding

class selectionGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH = 800
        CANVAS_SIZE_HEIGHT = 500

        # root
        self.root = tkinter.Tk()
        self.root.title("SELECTION")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)

        # PhotoImage(왼쪽 이미지)
        left_image = tkinter.PhotoImage(file="../image/SelectionDecode.png")
        label_img = tkinter.Label(self.root, image=left_image)
        label_img.place(x=150, y=120)

        # button(DECODING)
        button_decoding = tkinter.Button(self.root, text="DECODING", width=12, foreground="#ffffff", font=("roboto", "15"), background="#000000",
                                      relief="flat", command=lambda: self.decodingClick())
        button_decoding.place(x=140, y=300)

        # PhotoImage(오른쪽 이미지)
        right_image = tkinter.PhotoImage(file="../image/SelectionEncode.png")
        label_img = tkinter.Label(self.root, image=right_image)
        label_img.place(x=520, y=120)

        # button(ENCODING)
        button_encoding = tkinter.Button(self.root, text="ENCODING", width=12, foreground="#ffffff", font=("roboto", "15"),
                                         background="#000000", relief="flat", command=lambda: self.encodingClick())
        button_encoding.place(x=518, y=300)

        self.root.mainloop()

    def decodingClick(self):
        from GUI.decode import decodeGUI
        self.root.destroy()
        decodeGUI()

    def encodingClick(self):
        from GUI.encode import encodeGUI
        self.root.destroy()
        encodeGUI()


if __name__ == '__main__':
    selectionGUI = selectionGUI()
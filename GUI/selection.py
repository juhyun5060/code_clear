import tkinter
import tkinter.messagebox
import os
import sys

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
        left_image = tkinter.PhotoImage(file=os.path.join(os.path.abspath('../image'), 'SelectionDecode.png'))
        label_img = tkinter.Label(self.root, image=left_image)
        label_img.place(x=150, y=120)

        # button(DECODING)
        button_decoding = tkinter.Button(self.root, text="DECODING", width=12, foreground="#ffffff", font=("roboto", "15"), background="#000000",
                                      relief="flat", command=lambda: self.decodingClick())
        button_decoding.place(x=140, y=300)

        # PhotoImage(오른쪽 이미지)
        right_image = tkinter.PhotoImage(file=os.path.join(os.path.abspath('../image'), 'SelectionEncode.png'))
        label_img = tkinter.Label(self.root, image=right_image)
        label_img.place(x=520, y=120)

        # button(ENCODING)
        button_encoding = tkinter.Button(self.root, text="ENCODING", width=12, foreground="#ffffff", font=("roboto", "15"),
                                         background="#000000", relief="flat", command=lambda: self.encodingClick())
        button_encoding.place(x=518, y=300)

        self.root.protocol('WM_DELETE_WINDOW', self.doSomething)

        self.root.mainloop()

    def decodingClick(self):
        tkinter.messagebox.showinfo("공사중", "더 좋은 복호화로 돌아오겠습니다!")

    def encodingClick(self):
        from GUI.encode import encodeGUI
        self.root.destroy()
        encodeGUI()

    def doSomething(self):
        sys.exit()

if __name__ == '__main__':
    selectionGUI = selectionGUI()
import tkinter

class MainGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH = 800
        CANVAS_SIZE_HEIGHT = 500

        # root
        self.root = tkinter.Tk()
        self.root.title("CODE CLEAR")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)

        # label(CODE)
        label_code = tkinter.Label(self.root, text="CODE", font=("roboto", "40", 'bold'))
        label_code.place(x=135, y=95)

        # PhotoImage(자물쇠 이미지)
        lock_img = tkinter.PhotoImage(file="../image/lock.png")
        label_img = tkinter.Label(self.root, image=lock_img)
        label_img.pack(pady=65)

        # label(CLEAR)
        label_clear = tkinter.Label(self.root, text="CLEAR", font=("roboto", "40", 'bold'))
        label_clear.place(x=500, y=90)

        # label(한줄 문구)
        label_ment = tkinter.Label(self.root, text="암호의 세계로 빠져보세요", font=(30))
        label_ment.pack()

        # button(START)
        button_start = tkinter.Button(self.root, text="START", width=15, foreground="#ffffff", font=("roboto", "15"), background="#000000",
                                      relief="flat", command=lambda: self.startClick())
        button_start.pack(side='bottom', pady=90)

        self.root.mainloop()

    def startClick(self):
        from GUI.selection import selectionGUI
        self.root.destroy()
        selectionGUI()

if __name__ == '__main__':
    MainGUI = MainGUI()
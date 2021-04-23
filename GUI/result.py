import tkinter

class ResultGUI:
    def __init__(self, encoded_str):
        CANVAS_SIZE_WIDTH = 800
        CANVAS_SIZE_HEIGHT = 500

        # root
        self.root = tkinter.Tk()
        self.root.title("RESULT")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)

        # PhotoImage
        code_image = tkinter.PhotoImage(file="../image/code.png")
        label_img = tkinter.Label(self.root, image=code_image)
        label_img.pack(pady=30)

        # label(Comment)
        label_cmt = tkinter.Label(self.root, text="The result is ... ", font=("roboto", 20))
        label_cmt.pack()

        # label(result)
        label_result = tkinter.Label(self.root, text=encoded_str, font=("roboto", 20), background="#ffffff")
        label_result.pack()

        # button(MAIN)
        button_main = tkinter.Button(self.root, text="MAIN", width=15, foreground="#ffffff", font=("roboto", "15"),
                                      background="#000000",
                                      relief="flat", command=lambda: self.mainClick())
        button_main.place(x=570, y=400)

        self.root.mainloop()

    def mainClick(self):
        from GUI.main import MainGUI
        self.root.destroy()
        MainGUI()

if __name__ == '__main__':
    ResultGUI = ResultGUI()
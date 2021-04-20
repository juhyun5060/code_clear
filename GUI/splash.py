import tkinter
from GUI.main import MainGUI

class SplashGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH = 800
        CANVAS_SIZE_HEIGHT = 500

        # root
        self.root = tkinter.Tk()
        self.root.title("CODE CLEAR")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)

        # PhotoImage
        splash_img = tkinter.PhotoImage(file="../image/loading.png")
        loading_img = tkinter.Label(image=splash_img)
        loading_img.pack(pady=90)

        # label(LOADING...)
        label_loading = tkinter.Label(text="LOADING ...", font=("roboto", "30"))
        label_loading.pack()

        self.root.after(2000, MainGUI())

if __name__ == '__main__':
    SplashGUI = SplashGUI()
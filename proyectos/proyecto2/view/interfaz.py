from tkinter import *
class Ventana :
    def __init__(self,root):
        self.root = root
        self.root.title("proyecto 2")
        self.root.config(bg="red")  
        self.root.geometry("900x800+450+50")

        self.cuadrado =Label(root,width=30,height=10,bg="blue")
        self.cuadrado.place(x=100,y=100)


if __name__ == "__main__":
    ventana = Tk()
    app = Ventana(ventana)
    ventana.mainloop()
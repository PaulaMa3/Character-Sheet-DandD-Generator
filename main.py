import tkinter as tk
from view import MainWindow

def main():
    root = tk.Tk()
    root.title("Generador de Fichas de Personaje")
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()




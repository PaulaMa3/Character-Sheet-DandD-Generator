import tkinter as tk
from ttkthemes import ThemedTk
from view import MainWindow

def main():
    root = ThemedTk(theme="yaru")
    root.title("Generador de Fichas de Personaje")
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()

from ttkthemes import ThemedTk
from view import MainWindow
from db import init_db

def main():
    init_db()
    root = ThemedTk(theme="yaru")
    root.title("Generador de Fichas de Personaje")
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()

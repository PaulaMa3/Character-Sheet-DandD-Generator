import tkinter as tk
from tkinter import ttk
from add_character import AddCharacter
from see_character import SeeCharacter

class MainWindow:
    db_characters = 'database/characters.db'
    db_races = 'database/races.db'
    db_classes = 'database/classes.db'
    db_skills = 'database/skills.db'

    def __init__(self, root):
        self.window = root
        self.window.title("Generador de Fichas de Personaje")
        # Establecer tamaño de la ventana a 1280x1024
        self.window.geometry("1280x1024")
        self.window.resizable(1, 1)
        self.window.wm_iconbitmap('resources/icon.ico')

        # Configuración de estilos:
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background='#DBE1BC', foreground='black', font=('Garamond', 13), borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('TButton', background=[('active', '#adc178')])
        style.configure('TEntry', font=('Garamond', 11), padding=3)
        style.configure('Custom.TLabelframe', background='#FEFAE0', relief="sunken")
        style.configure('Custom.TLabelframe.Label', foreground='#6c584c', background='#FEFAE0', font=('Garamond', 20, 'bold'))
        style.configure('Custom.TFrame', background='#FEFAE0', relief="flat")
        style.configure('MessageBox.TFrame', background='#FEFAE0')

        # Otros botones
        style.configure('Light.TButton', background='#E7C8A0', foreground='black', font=('Garamond', 13), borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('Light.TButton', background=[('active', '#D4A373')])

        style.configure('Dark.TButton', background='#e5383b', foreground='white', font=('Garamond', 13), borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('Dark.TButton', background=[('active', '#540804')])

        # Configurar columnas y filas en la ventana principal
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        # Creación del contenedor Frame principal utilizando ttk.LabelFrame
        self.main_frame = ttk.LabelFrame(self.window, text=" INICIO ", labelanchor='n', style='Custom.TLabelframe')
        self.main_frame.grid(row=0, column=0, columnspan=3, pady=(35, 5), padx=5, sticky=tk.NSEW)

        # Configurar columnas para que se expandan correctamente
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)

        # Botón de crear nuevo personaje, editar o ver personajes utilizando ttk.Button
        self.boton_crear = ttk.Button(self.main_frame, text='Crear personaje', command=self.show_add_character)
        self.boton_crear.grid(row=2, column=1, padx=20, pady=(30, 10), sticky=tk.W + tk.E)
        self.boton_ver = ttk.Button(self.main_frame, text='Lista de personajes', command=self.show_see_character)
        self.boton_ver.grid(row=3, column=1, padx=20, pady=(10, 30), sticky=tk.W + tk.E)
        self.boton_salir = ttk.Button(self.main_frame, text='Salir', command=self.window.quit, style= "Dark.TButton")
        self.boton_salir.grid(row=4, column=1, padx=20, pady=(10, 30), sticky=tk.W + tk.E)

        # Inicializar el Frame de AddCharacter pero no mostrarlo todavía
        self.add_character_frame = AddCharacter(self.window, self)
        self.add_character_frame.grid(row=0, column=0, columnspan=3, pady=(5, 20), padx=20, sticky=tk.W + tk.E)
        self.add_character_frame.grid_remove()

        # Inicializar el Frame de SeeCharacter pero no mostrarlo todavía
        self.see_character_frame = SeeCharacter(self.window, self)
        self.see_character_frame.grid(row=0, column=0, columnspan=3, pady=(5, 20), padx=20, sticky=tk.W + tk.E)
        self.see_character_frame.grid_remove()

        self.center_window()

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def show_add_character(self):
        self.main_frame.grid_remove()
        self.add_character_frame.grid()

    def show_see_character(self):
        self.main_frame.grid_remove()
        self.see_character_frame.grid()

    def show_main_window(self):
        self.add_character_frame.grid_remove()
        self.see_character_frame.grid_remove()
        self.main_frame.grid()

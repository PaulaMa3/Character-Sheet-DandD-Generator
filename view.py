import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class MainWindow:
    db = 'database/characters.db'

    def __init__(self, root):
        self.window = root
        self.window.title("Generador de Fichas de Personaje")
        self.window.resizable(1, 1)
        self.window.wm_iconbitmap('resources/icon.ico')

        # Configuración de estilos:
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background='#adc178', foreground='black', font=('Garamond', 13), borderwidth=1,
                        focusthickness=3, focuscolor='none')
        style.map('TButton', background=[('active', '#45a049')])
        style.configure('TEntry', font=('Garamond', 11), padding=3)
        style.configure('Custom.TLabelframe.Label', foreground='#6c584c', font=('Garamond', 16, 'bold'))

        # Creación del contenedor Frame principal utilizando ttk.LabelFrame
        self.main_frame = ttk.LabelFrame(self.window, text=" INICIO ", labelanchor='n', style='Custom.TLabelframe')
        self.main_frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky=tk.W + tk.E)

        # Botón de crear nuevo personaje, editar o ver personajes utilizando ttk.Button
        self.boton_crear = ttk.Button(self.main_frame, text='Crear personaje', command=self.show_add_character)
        self.boton_crear.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W + tk.E)
        self.boton_editar = ttk.Button(self.main_frame, text='Editar personaje')
        self.boton_editar.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W + tk.E)
        self.boton_ver = ttk.Button(self.main_frame, text='Ver personaje')
        self.boton_ver.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W + tk.E)

        # Inicializar el Frame de AddCharacter pero no mostrarlo todavía
        self.add_character_frame = AddCharacter(self.window)
        self.add_character_frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky=tk.W + tk.E)
        self.add_character_frame.grid_remove()

    def db_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(consulta, parametros)
            con.commit()
        return resultado

    def get_character(self):
        registros_tabla = self.tabla.get_children()
        for fila in registros_tabla:
            self.tabla.delete(fila)
        query = 'SELECT * FROM character ORDER BY name DESC'
        registros_db = self.db_consulta(query)

        for fila in registros_db:
            self.tabla.insert('', 0, text=fila[1], values=(fila[2], fila[3], fila[4]))

    def show_add_character(self):
        self.main_frame.grid_remove()
        self.add_character_frame.grid()


class AddCharacter(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        frame_ep = ttk.LabelFrame(self, text="Generador de fichas de personaje", style='Custom.TLabelframe')
        frame_ep.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky=tk.W + tk.E)

        # Crear un marco para la imagen y el botón
        self.image_frame = tk.Frame(frame_ep, width=150, height=150, bg="gray")
        self.image_frame.grid(row=0, column=0, rowspan=4, padx=5, pady=5, sticky=tk.NW)

        self.add_image_button = ttk.Button(self.image_frame, text="Agregar Imagen", command=self.select_image)
        self.add_image_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label_name = ttk.Label(frame_ep, text="Nombre:", font=("Garamond", 11))
        self.label_name.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_name = ttk.Entry(frame_ep, font=("Garamond", 11))
        self.entry_name.grid(row=0, column=2, padx=5, pady=5, sticky=tk.E)

        self.label_race = ttk.Label(frame_ep, text="Raza:", font=("Garamond", 11))
        self.label_race.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.races = ["Enano", "Elfo", "Mediano", "Humano", "Dracónido", "Gnomo", "Medio-elfo", "Medio-orco", "Tiefling"]
        self.combobox_race = ttk.Combobox(frame_ep, values=self.races, font=('Garamond', 11), state='readonly')
        self.combobox_race.grid(row=1, column=2, padx=5, pady=5, sticky=tk.E)

        self.label_class = ttk.Label(frame_ep, text="Clase:", font=("Garamond", 11))
        self.label_class.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.classes = ["Bárbaro", "Bardo", "Clérigo", "Druida", "Guerrero", "Monje", "Paladín", "Explorador", "Pícaro", "Hechicero", "Brujo", "Mago"]
        self.combobox_c_class = ttk.Combobox(frame_ep, values=self.classes, font=('Garamond', 11), state='readonly')
        self.combobox_c_class.grid(row=2, column=2, padx=5, pady=5, sticky=tk.E)

        self.label_level = ttk.Label(frame_ep, text="Nivel:", font=("Garamond", 11))
        self.label_level.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_level = ttk.Entry(frame_ep, font=("Garamond", 11))
        self.entry_level.grid(row=3, column=2, padx=5, pady=5, sticky=tk.E)

    def select_image(self):
        # Abrir cuadro de diálogo para seleccionar archivo
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])

        if file_path:
            # Cargar imagen usando PIL
            image = Image.open(file_path)
            image = image.resize((150, 150), Image.LANCZOS)  # Redimensionar imagen si es necesario
            photo = ImageTk.PhotoImage(image)

            # Reemplazar el botón con el widget de imagen
            self.add_image_button.place_forget()
            self.img_label = tk.Label(self.image_frame, image=photo)
            self.img_label.image = photo  # Mantener una referencia a la imagen para evitar que se elimine
            self.img_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


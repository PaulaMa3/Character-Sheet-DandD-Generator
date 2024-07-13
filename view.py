import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog, END
from PIL import Image, ImageTk
import db


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
        style.configure('TButton', background='#DDA15E', foreground='black', font=('Garamond', 13), borderwidth=1,
                        focusthickness=3, focuscolor='none')
        style.map('TButton', background=[('active', '#45a049')])
        style.configure('TEntry', font=('Garamond', 11), padding=3)
        style.configure('Custom.TLabelframe', background='#FEFAE0', relief="sunken")
        style.configure('Custom.TLabelframe.Label', foreground='#6c584c', background='#FEFAE0',
                        font=('Garamond', 20, 'bold'))
        style.configure('Custom.TFrame', background='#FEFAE0', relief="flat")

        # Botón de inicio
        style.configure('Light.TButton', background='#BC6C25', foreground='black', font=('Garamond', 13), borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('Light.TButton', background=[('active', '#1E8C7B')])

        style.configure('Green.TButton', background='#606C38', foreground='black', font=('Garamond', 13), borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('Green.TButton', background=[('active', '#4F5A2E')])

        # Creación del contenedor Frame principal utilizando ttk.LabelFrame
        self.main_frame = ttk.LabelFrame(self.window, text=" INICIO ", labelanchor='n', style='Custom.TLabelframe')
        self.main_frame.grid(row=0, column=0, columnspan=3, pady=(5, 5), padx=5, sticky=tk.W + tk.E)

        # Botón de crear nuevo personaje, editar o ver personajes utilizando ttk.Button
        self.boton_crear = ttk.Button(self.main_frame, text='Crear personaje', command=self.show_add_character)
        self.boton_crear.grid(row=2, column=0, padx=20, pady=(30, 10), sticky=tk.W + tk.E)
        self.boton_editar = ttk.Button(self.main_frame, text='Editar personaje')
        self.boton_editar.grid(row=3, column=0, padx=20, pady=10, sticky=tk.W + tk.E)
        self.boton_ver = ttk.Button(self.main_frame, text='Lista de personajes', command=self.show_see_character)
        self.boton_ver.grid(row=4, column=0, padx=20, pady=(10, 30), sticky=tk.W + tk.E)

        # Inicializar el Frame de AddCharacter pero no mostrarlo todavía
        self.add_character_frame = AddCharacter(self.window, self)
        self.add_character_frame.grid(row=0, column=0, columnspan=3, pady=(5, 20), padx=20, sticky=tk.W + tk.E)
        self.add_character_frame.grid_remove()

        # Inicializar el Frame de SeeCharacter pero no mostrarlo todavía
        self.see_character_frame = SeeCharacter(self.window, self)
        self.see_character_frame.grid(row=0, column=0, columnspan=3, pady=(5, 20), padx=20, sticky=tk.W + tk.E)
        self.see_character_frame.grid_remove()

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


class AddCharacter(ttk.Frame):
    db = 'database/characters.db'

    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.parent = parent
        self.main_window = main_window

        # Configurar un frame central que contenga todos los widgets
        central_frame = ttk.Frame(self)
        central_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")

        message_box = ttk.Frame(central_frame, style='Custom.TLabelframe')
        message_box.grid(row=0, column=0, padx=0, sticky="ew")

        self.ok_message = ttk.Label(message_box, text="", font=("Garamond", 15), background='#FEFAE0', foreground='green')
        self.ok_message.pack(side="top", fill="x")

        self.error_message = ttk.Label(message_box, text="", font=("Garamond", 15), background='#FEFAE0', foreground='red')
        self.error_message.pack(side="top", fill="x")

        barra = ttk.Frame(central_frame, style='Custom.TLabelframe')
        barra.grid(row=1, column=0, columnspan=2, pady=0, padx=0, sticky="ew")

        # Añadir botón Guardar
        self.save_button = ttk.Button(barra, text="Guardar", command=self.save_character)
        self.save_button.pack(side="left", padx=(0, 10))

        # Añadir botón Volver a Inicio
        self.back_button = ttk.Button(barra, text="Volver a Inicio", command=self.main_window.show_main_window)
        self.back_button.pack(side="left", padx=(10, 0))

        frame_ep = ttk.LabelFrame(central_frame, text="Generador de fichas de personaje", style='Custom.TLabelframe')
        frame_ep.grid(row=2, column=0, columnspan=1, pady=0, padx=0, sticky="nsew")

        # Crear un marco para la imagen y el botón
        self.image_frame = tk.Frame(frame_ep, width=150, height=150, bg="#FEFAE0")
        self.image_frame.grid(row=2, column=0, rowspan=4, padx=5, pady=5, sticky="nw")

        self.add_image_button = ttk.Button(self.image_frame, text="Agregar Imagen", command=self.select_image)
        self.add_image_button.place(relx=0.5, rely=0.5, anchor="center")

        self.label_name = ttk.Label(frame_ep, text="Nombre:", font=("Garamond", 15), background='#FEFAE0')
        self.label_name.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.entry_name = ttk.Entry(frame_ep, font=("Garamond", 15))
        self.entry_name.grid(row=2, column=2, padx=5, pady=5, sticky="e")

        self.label_race = ttk.Label(frame_ep, text="Raza:", font=("Garamond", 15), background='#FEFAE0')
        self.label_race.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.races = ["Enano", "Elfo", "Mediano", "Humano", "Dracónido", "Gnomo", "Medio-elfo", "Medio-orco",
                      "Tiefling"]
        self.combobox_race = ttk.Combobox(frame_ep, values=self.races, font=('Garamond', 15), state='readonly')
        self.combobox_race.grid(row=3, column=2, padx=5, pady=5, sticky="e")

        self.label_class = ttk.Label(frame_ep, text="Clase:", font=("Garamond", 15), background='#FEFAE0')
        self.label_class.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.classes = ["Bárbaro", "Bardo", "Clérigo", "Druida", "Guerrero", "Monje", "Paladín", "Explorador", "Pícaro",
                        "Hechicero", "Brujo", "Mago"]
        self.combobox_c_class = ttk.Combobox(frame_ep, values=self.classes, font=('Garamond', 15), state='readonly')
        self.combobox_c_class.grid(row=4, column=2, padx=5, pady=5, sticky="e")

        self.label_level = ttk.Label(frame_ep, text="Nivel:", font=("Garamond", 15), background='#FEFAE0')
        self.label_level.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.entry_level = ttk.Entry(frame_ep, font=("Garamond", 15))
        self.entry_level.grid(row=5, column=2, padx=5, pady=5, sticky="e")

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
            self.img_label.place(relx=0.5, rely=0.5, anchor="center")

    def db_query(self, consulta, parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(consulta, parametros)
            con.commit()
        return resultado

    def save_character(self):
        query = 'INSERT INTO characters (name, race, c_class, level) VALUES (?, ?, ?, ?)'
        parametros = (
            self.entry_name.get(), self.combobox_race.get(), self.combobox_c_class.get(), self.entry_level.get())
        self.db_query(query, parametros)
        self.ok_message['text'] = f'Personaje {self.entry_name.get()} añadido con éxito'
        self.entry_name.delete(0, tk.END)
        self.combobox_race.set('')
        self.combobox_c_class.set('')
        self.entry_level.delete(0, tk.END)


class SeeCharacter(ttk.Frame):
    db = 'database/characters.db'

    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.parent = parent
        self.main_window = main_window

        # Configurar un frame central que contenga todos los widgets
        self.central_frame = ttk.Frame(self)
        self.central_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")

        message_box = ttk.Frame(self.central_frame, style='Custom.TLabelframe')
        message_box.grid(row=0, column=0, padx=0, sticky="ew")

        self.ok_message = ttk.Label(message_box, text="", font=("Garamond", 15), foreground='green')
        self.ok_message.pack(side="top", fill="x")

        self.error_message = ttk.Label(message_box, text="", font=("Garamond", 15), foreground='red')
        self.error_message.pack(side="top", fill="x")

        # Añadir barra de búsqueda
        self.search_entry = ttk.Entry(self.central_frame, font=('Garamond', 15))
        self.search_entry.grid(row=1, column=0, padx=10, pady=0, sticky=tk.W + tk.E, columnspan=2)

        # Crear un frame para los botones
        button_frame = ttk.Frame(self.central_frame, style='Custom.TLabelframe')
        button_frame.grid(row=1, column=2, padx=5, pady=(0, 5), sticky="ne")

        self.search_button = ttk.Button(button_frame, text="Buscar", command=self.search_character, style='Light.TButton')
        self.search_button.grid(row=0, column=0, padx=5)

        self.delete_button = ttk.Button(button_frame, text="Eliminar", command=self.del_character, style='Light.TButton')
        self.delete_button.grid(row=0, column=1, padx=5)

        self.back_button = ttk.Button(button_frame, text="Volver", command=self.main_window.show_main_window, style='Light.TButton')
        self.back_button.grid(row=0, column=2, padx=5)

        # Inicializar la tabla donde se mostrarán los resultados
        self.tabla = ttk.Treeview(self.central_frame, columns=("Name", "Race", "Class", "Level"), show='headings')
        self.tabla.heading("Name", text="Nombre")
        self.tabla.heading("Race", text="Raza")
        self.tabla.heading("Class", text="Clase")
        self.tabla.heading("Level", text="Nivel")
        self.tabla.grid(row=2, column=0, columnspan=3, padx=0, pady=0, sticky=tk.W + tk.E)
        self.get_character()

    def search_character(self):
        search_term = self.search_entry.get()
        query = 'SELECT * FROM characters WHERE name LIKE ? ORDER BY name DESC'
        registros_db = self.db_consulta(query, ('%' + search_term + '%',))

        # Limpiar la tabla actual y mostrar los resultados de la búsqueda
        self.tabla.delete(*self.tabla.get_children())
        for fila in registros_db:
            self.tabla.insert('', 0, values=(fila[1], fila[2], fila[3], fila[4]))

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
        query = 'SELECT * FROM characters ORDER BY name DESC'
        registros_db = self.db_consulta(query)

        for fila in registros_db:
            self.tabla.insert('', 0, values=(fila[1], fila[2], fila[3], fila[4]))

    def del_character(self):
        self.ok_message['text'] = ''
        self.error_message['text'] = ''
        try:
            nombre = self.tabla.item(self.tabla.selection())['values'][0]
        except IndexError:
            self.error_message['text'] = 'Por favor, seleccione un personaje'
            return

        query = 'DELETE FROM characters WHERE name = ?'
        self.db_consulta(query, (nombre,))
        self.ok_message['text'] = f'Personaje {nombre} eliminado con éxito'
        self.get_character()

import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from db_utils import get_races, get_classes



class MainWindow:
    db_characters = 'database/characters.db'
    db_races = 'database/races.db'
    db_classes = 'database/classes.db'
    db_skills = 'database/skills.db'

    def __init__(self, root):
        self.window = root
        self.window.title("Generador de Fichas de Personaje")
        self.window.attributes('-fullscreen', True)  # Pantalla completa
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


class AddCharacter(ttk.Frame):
    db_characters = 'database/characters.db'
    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.parent = parent
        self.main_window = main_window

        # Configurar un frame central que contenga todos los widgets
        central_frame = ttk.Frame(self, style='Custom.TFrame')
        central_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        central_frame.columnconfigure(0, weight=1)

        message_box = ttk.Frame(central_frame, style='MessageBox.TFrame')
        message_box.grid(row=0, column=0, padx=0, sticky="ew", columnspan=3)

        self.ok_message = ttk.Label(message_box, text="", font=("Garamond", 15), background='#FEFAE0',
                                    foreground='green')
        self.ok_message.grid(row=0, column=0, sticky="ew")

        self.error_message = ttk.Label(message_box, text="", font=("Garamond", 15), background='#FEFAE0',
                                       foreground='red')
        self.error_message.grid(row=1, column=0, sticky="ew")

        barra = ttk.Frame(central_frame, style='Custom.TFrame')
        barra.grid(row=1, column=0, columnspan=2, pady=(0, 15), padx=0, sticky="ew")

        # Añadir botón Guardar
        self.save_button = ttk.Button(barra, text="Guardar", command=self.save_character)
        self.save_button.pack(side="left", padx=(0, 10))

        # Añadir botón Volver a Inicio
        self.back_button = ttk.Button(barra, text="Volver a Inicio", command=self.main_window.show_main_window,
                                      style="Light.TButton")
        self.back_button.pack(side="left", padx=(10, 0))

        frame_ep = ttk.LabelFrame(central_frame, text="Generador de fichas de personaje", style='Custom.TLabelframe')
        frame_ep.grid(row=2, column=0, columnspan=1, pady=0, padx=0, sticky="nsew")

        # Crear un marco para la imagen y el botón
        self.image_frame = tk.Frame(frame_ep, width=150, height=150, bg="gray")
        self.image_frame.grid(row=2, column=0, rowspan=4, padx=5, pady=5, sticky="nw")

        self.add_image_button = ttk.Button(self.image_frame, text="Agregar Imagen", command=self.select_image)
        self.add_image_button.place(relx=0.5, rely=0.5, anchor="center")

        self.label_name = ttk.Label(frame_ep, text="Nombre:", font=("Garamond", 15), background='#FEFAE0')
        self.label_name.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.entry_name = ttk.Entry(frame_ep, font=("Garamond", 15))
        self.entry_name.grid(row=2, column=2, padx=5, pady=5, sticky="e")

        self.label_race = ttk.Label(frame_ep, text="Raza:", font=("Garamond", 15), background='#FEFAE0')
        self.label_race.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.combobox_race = ttk.Combobox(frame_ep, values=get_races(), font=('Garamond', 15), state='readonly')
        self.combobox_race.grid(row=3, column=2, padx=5, pady=5, sticky="e")

        self.label_class = ttk.Label(frame_ep, text="Clase:", font=("Garamond", 15), background='#FEFAE0')
        self.label_class.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.combobox_c_class = ttk.Combobox(frame_ep, values=get_classes(), font=('Garamond', 15), state='readonly')
        self.combobox_c_class.grid(row=4, column=2, padx=5, pady=5, sticky="e")

        self.label_level = ttk.Label(frame_ep, text="Nivel:", font=("Garamond", 15), background='#FEFAE0')
        self.label_level.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.entry_level = ttk.Entry(frame_ep, font=("Garamond", 15))
        self.entry_level.grid(row=5, column=2, padx=5, pady=5, sticky="e")

        # Atributos
        attributes = ttk.Frame(central_frame, style='Custom.TFrame')
        attributes.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Fuerza
        strength = ttk.Frame(attributes, style='Custom.TFrame')
        strength.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.strength_label = ttk.Label(strength, text="Fuerza", font=("Garamond", 15), background='#FEFAE0')
        self.strength_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.strength_entry = ttk.Entry(strength, font=("Garamond", 15), width=5)
        self.strength_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.strength_info = ttk.Label(strength, text="", font=("Garamond", 10), background='#FEFAE0')
        self.strength_info.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        # Destreza
        dexterity = ttk.Frame(attributes, style='Custom.TFrame')
        dexterity.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.dexterity_label = ttk.Label(dexterity, text="Destreza", font=("Garamond", 15), background='#FEFAE0')
        self.dexterity_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.dexterity_entry = ttk.Entry(dexterity, font=("Garamond", 15), width=5)
        self.dexterity_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.dexterity_info = ttk.Label(dexterity, text="", font=("Garamond", 10), background='#FEFAE0')
        self.dexterity_info.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        # Constitución
        constitution = ttk.Frame(attributes, style='Custom.TFrame')
        constitution.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.constitution_label = ttk.Label(constitution, text="Constitución", font=("Garamond", 15),
                                            background='#FEFAE0')
        self.constitution_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.constitution_entry = ttk.Entry(constitution, font=("Garamond", 15), width=5)
        self.constitution_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.constitution_info = ttk.Label(constitution, text="", font=("Garamond", 10), background='#FEFAE0')
        self.constitution_info.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        # Inteligencia
        intelligence = ttk.Frame(attributes, style='Custom.TFrame')
        intelligence.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.intelligence_label = ttk.Label(intelligence, text="Inteligencia", font=("Garamond", 15),
                                            background='#FEFAE0')
        self.intelligence_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.intelligence_entry = ttk.Entry(intelligence, font=("Garamond", 15), width=5)
        self.intelligence_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.intelligence_info = ttk.Label(intelligence, text="", font=("Garamond", 10), background='#FEFAE0')
        self.intelligence_info.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        # Sabiduría
        wisdom = ttk.Frame(attributes, style='Custom.TFrame')
        wisdom.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.wisdom_label = ttk.Label(wisdom, text="Sabiduría", font=("Garamond", 15), background='#FEFAE0')
        self.wisdom_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.wisdom_entry = ttk.Entry(wisdom, font=("Garamond", 15), width=5)
        self.wisdom_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.wisdom_info = ttk.Label(wisdom, text="", font=("Garamond", 10), background='#FEFAE0')
        self.wisdom_info.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        # Carisma
        charisma = ttk.Frame(attributes, style='Custom.TFrame')
        charisma.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.charisma_label = ttk.Label(charisma, text="Carisma", font=("Garamond", 15), background='#FEFAE0')
        self.charisma_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.charisma_entry = ttk.Entry(charisma, font=("Garamond", 15), width=5)
        self.charisma_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.charisma_info = ttk.Label(charisma, text="", font=("Garamond", 10), background='#FEFAE0')
        self.charisma_info.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        #Segundo Frame
        second_frame = ttk.Frame(central_frame, style='Custom.TFrame')
        second_frame.grid(row=6, column=3, columnspan=3, padx=5, pady=5, sticky="ew")

        self.armor_class_label = ttk.Label(second_frame, text="Clase de armadura", font=("Garamond", 15),background='#FEFAE0' )
        self.armor_class_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.armor_class_info_label = ttk.Label(second_frame, text="", font=("Garamond", 10), background='#FEFAE0')
        self.armor_class_info_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.initiative_label = ttk.Label(second_frame, text="Iniciativa", font=("Garamond", 15), background='#FEFAE0' )
        self.initiative_label.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.initiative_info_label = ttk.Label(second_frame, text="", font=("Garamond", 10), background='#FEFAE0')
        self.initiative_info_label.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        self.speed_label = ttk.Label(second_frame, text="Velocidad", font=("Garamond", 15), background='#FEFAE0')
        self.speed_label.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        self.speed_info_label = ttk.Label(second_frame, text="", font=("Garamond", 10), background='#FEFAE0')
        self.speed_info_label.grid(row=1, column=3, padx=5, pady=5, sticky="e")

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
        with sqlite3.connect(self.db_characters) as con:
            cursor = con.cursor()
            resultado = cursor.execute(consulta, parametros)
            con.commit()
        return resultado

    def validate_attributes(self):
        try:
            attributes = [
                int(self.strength_entry.get()),
                int(self.dexterity_entry.get()),
                int(self.constitution_entry.get()),
                int(self.intelligence_entry.get()),
                int(self.wisdom_entry.get()),
                int(self.charisma_entry.get())
            ]
        except ValueError:
            self.error_message['text'] = 'Todos los atributos deben ser números enteros.'
            return False

        total_sum = sum(attributes)

        if any(attr < 8 or attr > 15 for attr in attributes):
            self.error_message['text'] = 'Cada atributo debe estar entre 8 y 15.'
            return False

        if total_sum != 75:
            self.error_message[
                'text'] = f'La suma de todos los atributos debe ser exactamente 75. Actualmente sumas {total_sum} puntos.'
            return False

        self.error_message['text'] = ''
        return True

    def save_character(self):
        if not self.validate_attributes():
            return

        # Insertar nuevo personaje en la tabla characters
        query = 'INSERT INTO characters (name, race, c_class, level) VALUES (?, ?, ?, ?)'
        parametros = (
        self.entry_name.get(), self.combobox_race.get(), self.combobox_c_class.get(), self.entry_level.get())
        self.db_query(query, parametros)

        # Obtener el ID del personaje recién creado
        character_id = self.db_query('SELECT last_insert_rowid()').fetchone()[0]

        # Lista de atributos con sus valores correspondientes
        attributes = [
            ('Fuerza', self.strength_entry.get()),
            ('Destreza', self.dexterity_entry.get()),
            ('Constitución', self.constitution_entry.get()),
            ('Inteligencia', self.intelligence_entry.get()),
            ('Sabiduría', self.wisdom_entry.get()),
            ('Carisma', self.charisma_entry.get())
        ]

        # Insertar atributos en la tabla intermedia attribute_character_association junto con sus valores
        for attr_name, attr_value in attributes:
            attr_id = self.db_query('SELECT id FROM attributes WHERE name = ?', (attr_name,)).fetchone()[0]
            self.db_query(
                'INSERT INTO attribute_character_association (attribute_id, character_id, value) VALUES (?, ?, ?)',
                (attr_id, character_id, attr_value))

        # Mostrar un mensaje de éxito y limpiar los campos del formulario
        self.ok_message['text'] = f'Personaje {self.entry_name.get()} añadido con éxito'
        self.entry_name.delete(0, tk.END)
        self.combobox_race.set('')
        self.combobox_c_class.set('')
        self.entry_level.delete(0, tk.END)
        self.strength_entry.delete(0, tk.END)
        self.dexterity_entry.delete(0, tk.END)
        self.constitution_entry.delete(0, tk.END)
        self.intelligence_entry.delete(0, tk.END)
        self.wisdom_entry.delete(0, tk.END)
        self.charisma_entry.delete(0, tk.END)

class SeeCharacter(ttk.Frame):
    db_characters = 'database/characters.db'
    db_races = 'database/races.db'
    db_classes = 'database/classes.db'
    db_skills = 'database/skills.db'

    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.parent = parent
        self.main_window = main_window

        # Configurar un frame central que contenga todos los widgets
        self.central_frame = ttk.Frame(self, style='Custom.TFrame')
        self.central_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        self.central_frame.columnconfigure(0, weight=1)

        message_box = ttk.Frame(self.central_frame, style='Custom.TLabelframe')
        message_box.grid(row=0, column=0, padx=0, sticky="ew", columnspan=3)

        self.ok_message = ttk.Label(message_box, text="", font=("Garamond", 15), foreground='green', background='#FEFAE0')
        self.ok_message.grid(row=0, column=0, sticky="ew")

        self.error_message = ttk.Label(message_box, text="", font=("Garamond", 15), foreground='red', background='#FEFAE0')
        self.error_message.grid(row=1, column=0, sticky="ew")

        # Añadir barra de búsqueda
        self.search_entry = ttk.Entry(self.central_frame, font=('Garamond', 15))
        self.search_entry.grid(row=1, column=0, padx=10, pady=0, sticky=tk.W + tk.E, columnspan=2)

        # Crear un frame para los botones
        button_frame = ttk.Frame(self.central_frame, style='Custom.TFrame')
        button_frame.grid(row=1, column=2, padx=5, pady=(0, 5), sticky="ne")

        self.search_button = ttk.Button(button_frame, text="Buscar", command=self.search_character, style='TButton')
        self.search_button.grid(row=0, column=0, padx=5)

        self.delete_button = ttk.Button(button_frame, text="Eliminar", command=self.del_character, style='Dark.TButton')
        self.delete_button.grid(row=0, column=1, padx=5)

        self.back_button = ttk.Button(button_frame, text="Volver", command=self.main_window.show_main_window, style='Light.TButton')
        self.back_button.grid(row=0, column=2, padx=5)

        # Inicializar la tabla donde se mostrarán los resultados
        self.tabla = ttk.Treeview(self.central_frame, columns=("Name", "Race", "Class", "Level", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"), show='headings')
        self.tabla.heading("Name", text="Nombre")
        self.tabla.heading("Race", text="Raza")
        self.tabla.heading("Class", text="Clase")
        self.tabla.heading("Level", text="Nivel")
        self.tabla.heading("Strength", text="Fuerza")
        self.tabla.heading("Dexterity", text="Destreza")
        self.tabla.heading("Constitution", text="Constitución")
        self.tabla.heading("Intelligence", text="Inteligencia")
        self.tabla.heading("Wisdom", text="Sabiduría")
        self.tabla.heading("Charisma", text="Carisma")

        # Establecer el ancho de las columnas
        self.tabla.column("Name", width=100)
        self.tabla.column("Race", width=100)
        self.tabla.column("Class", width=100)
        self.tabla.column("Level", width=60)
        self.tabla.column("Strength", width=60)
        self.tabla.column("Dexterity", width=60)
        self.tabla.column("Constitution", width=80)
        self.tabla.column("Intelligence", width=80)
        self.tabla.column("Wisdom", width=60)
        self.tabla.column("Charisma", width=60)

        self.tabla.grid(row=2, column=0, columnspan=3, padx=0, pady=0, sticky=tk.W + tk.E)
        self.get_character()

    def search_character(self):
        search_term = self.search_entry.get()
        query = 'SELECT * FROM characters WHERE name LIKE ? ORDER BY name DESC'
        registros_db = self.db_consulta(query, ('%' + search_term + '%',))

        # Limpiar la tabla actual y mostrar los resultados de la búsqueda
        self.tabla.delete(*self.tabla.get_children())
        for fila in registros_db:
            self.tabla.insert('', 0, values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10]))

    def db_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db_characters) as con:
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
            self.tabla.insert('', 0, values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10]))

    def del_character(self):
        try:
            selected_item = self.tabla.selection()[0]
        except IndexError:
            self.error_message['text'] = 'Por favor, seleccione un personaje'
            return

        nombre = self.tabla.item(selected_item)['values'][0]
        query = 'DELETE FROM characters WHERE name = ?'
        self.db_consulta(query, (nombre,))
        self.ok_message['text'] = f'Personaje {nombre} eliminado con éxito'
        self.get_character()

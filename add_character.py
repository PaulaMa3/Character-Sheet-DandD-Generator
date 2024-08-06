import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from db_utils import get_races, get_classes, get_class_armor


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

        # Obtener detalles de las razas
        self.race_bonuses = get_races()

        self.combobox_race = ttk.Combobox(frame_ep, values=list(self.race_bonuses.keys()), font=('Garamond', 15),
                                          state='readonly')
        self.combobox_race.grid(row=3, column=2, padx=5, pady=5, sticky="e")

        # Configurar combobox_race con el comando para actualizar bonificaciones
        self.combobox_race.bind("<<ComboboxSelected>>", self.update_attribute_bonuses)

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

        # Segundo Frame
        second_frame = ttk.Frame(attributes, style='Custom.TFrame')
        second_frame.grid(row=0, column=1, rowspan=6, padx=5, pady=5, sticky="nsew")

        self.armor_class_label = ttk.Label(second_frame, text="Clase de armadura", font=("Garamond", 15),
                                           background='#FEFAE0')
        self.armor_class_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.armor_class_info_label = ttk.Label(second_frame, text="", font=("Garamond", 10), background='#FEFAE0')
        self.armor_class_info_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.initiative_label = ttk.Label(second_frame, text="Iniciativa", font=("Garamond", 15), background='#FEFAE0')
        self.initiative_label.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.initiative_info_label = ttk.Label(second_frame, text="", font=("Garamond", 10), background='#FEFAE0')
        self.initiative_info_label.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        self.speed_label = ttk.Label(second_frame, text="Velocidad", font=("Garamond", 15), background='#FEFAE0')
        self.speed_label.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        self.speed_info_label = ttk.Label(second_frame, text="", font=("Garamond", 10), background='#FEFAE0')
        self.speed_info_label.grid(row=1, column=3, padx=5, pady=5, sticky="e")

        #Equipamiento y armas
        equipment_frame = ttk.Frame(attributes, style='Custom.TFrame')
        equipment_frame.grid(row=0, column=2, rowspan=6, columnspan=2, padx=5, pady=5, sticky="nsew" )

        self.combobox_c_class.bind("<<ComboboxSelected>>", self.update_equipment)

        self.equipment_label = ttk.Label (equipment_frame, text="Armadura", font=("Garamond", 15), background='#FEFAE0' )
        self.equipment_label.grid(row=0, column=1, columnspan=3, padx=(15, 5), pady=5, sticky="e" )
        self.equipment_info_label = ttk.Label(equipment_frame, text="", font=("Garamond", 10), background='#FEFAE0')
        self.equipment_info_label.grid(row=1, column=1,  columnspan=3, padx=(15, 5), pady=5, sticky="e")

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

    def update_attribute_bonuses(self, event=None):
        selected_race = self.combobox_race.get()
        bonuses = self.race_bonuses.get(selected_race, {})

        self.strength_info.config(text=f"+{bonuses.get('Fuerza', 0)}")
        self.dexterity_info.config(text=f"+{bonuses.get('Destreza', 0)}")
        self.constitution_info.config(text=f"+{bonuses.get('Constitución', 0)}")
        self.intelligence_info.config(text=f"+{bonuses.get('Inteligencia', 0)}")
        self.wisdom_info.config(text=f"+{bonuses.get('Sabiduría', 0)}")
        self.charisma_info.config(text=f"+{bonuses.get('Carisma', 0)}")

    def update_equipment(self, event=None):
        selected_class = self.combobox_c_class.get()
        armor_name = get_class_armor(selected_class)
        self.equipment_info_label.config(text=armor_name)

    """def update_armor_class(self, event=None):
        selected_class = self.combobox_c_class.get()
        armor_class = self.class_armor_class

        self.armor_class_info.config(text=f"{armor_class.get('Armor Class', 0)}")"""

    def save_character(self):
        if not self.validate_attributes():
            return

        # Insertar nuevo personaje en la tabla characters
        query = 'INSERT INTO characters (name, race_id, class_id, level) VALUES (?, ?, ?, ?)'
        parametros = (
            self.entry_name.get(), self.combobox_race.get(), self.combobox_c_class.get(), self.entry_level.get())

        # Ejecutar la consulta de inserción y obtener el ID del personaje recién creado
        with sqlite3.connect(self.db_characters) as con:
            cursor = con.cursor()
            cursor.execute(query, parametros)
            character_id = cursor.lastrowid
            con.commit()

        print(f"Character ID: {character_id}")

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
            attr_id = self.db_query('SELECT id FROM attributes WHERE name = ?', (attr_name,)).fetchone()
            if attr_id:  # Asegurarse de que se obtuvo un resultado
                attr_id = attr_id[0]  # Obtener el valor entero
                self.db_query(
                    'INSERT INTO attribute_character_association (attribute_id, character_id, value) VALUES (?, ?, ?)',
                    (attr_id, character_id, attr_value)
                )

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

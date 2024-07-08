import tkinter as tk
from tkinter import ttk
from db import session
from models import Character
import db

class MainWindow:
    db = 'database/characters.db'

    def __init__(self, root):
        self.window = root
        self.window.resizable(1, 1)
        self.window.wm_iconbitmap('resources/icon.ico')

        # Configuración de estilos:
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background='#adc178', foreground='black', font=('Garamond', 13), borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('TButton', background=[('active', '#45a049')])
        style.configure('TEntry', font=('Garamond', 13), padding=5)
        style.configure('Custom.TLabelframe.Label', foreground='#6c584c', font=('Garamond', 16, 'bold'))

        # Creación del contenedor Frame principal utilizando ttk.LabelFrame
        frame = ttk.LabelFrame(self.window, text=" INICIO ", labelanchor='n', style='Custom.TLabelframe')
        frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky=tk.W + tk.E)

        # Botón de crear nuevo personaje, editar o ver personajes utilizando ttk.Button
        self.boton_crear = ttk.Button(frame, text='Crear personaje')
        self.boton_crear.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W + tk.E)
        self.boton_editar = ttk.Button(frame, text='Editar personaje')
        self.boton_editar.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W + tk.E)
        self.boton_ver = ttk.Button(frame, text='Ver personaje')
        self.boton_ver.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W + tk.E)






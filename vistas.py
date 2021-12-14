from tkinter import Frame, Label, Text, Entry
from tkinter.messagebox import showerror
from tkinter import ttk
from datetime import datetime
from modelo import Funciones_abmc, Servidor

from estilos.estilos import Estilos
from guardar.guardar import guardar_proveedor


class Vistas_app_proveedores(Funciones_abmc):
    """Clase que contiene la estructura de la seccion proveedores y hereda de Funciones_abmc"""

    def __init__(self, ventana):
        self.root2 = ventana
        self.root2.title("Ventana Principal - PROVEEDORES")
        self.root2.iconbitmap("logoJamon.ico")
        self.root2.config(bg="black")
        self.root2.geometry('1215x625+5+5')

        """ por medio del objeto se llaman a los estilos que estan modulados en la carpeta estilos"""
        objeto_estilos = Estilos()
        objeto_estilos.estilo_botones()
        objeto_estilos.estilos_combos()
        objeto_estilos.estilo_btn_cerrar()
        objeto_estilos.estilo_tree()

        try:
            titulo = Frame(self.root2, bg="red3",
                           borderwidth=4, relief="ridge")
            titulo.grid(row=0, column=0, pady=2)
            lbl_titulo = Label(titulo, text='Administracion de Proveedores', padx=14, pady=10, font=(
                "arial", 20, "bold"), fg="white", bg="gray20")
            lbl_titulo.grid(row=0, column=0)

            """ BOTONES DEL SERVIDOR """

            ttk.Button(titulo, text="Activar Server", command=lambda: Servidor.activa_server()).grid(
                row=0, column=1, padx=15, pady=10, sticky="we")
            ttk.Button(titulo, text="Parar Server", command=lambda: Servidor.stop_server()).grid(
                row=0, column=2, padx=15, pady=10, sticky="we")
            # ##########################################################

            def hora():
                fecha = datetime.now()
                format = fecha.strftime('%d/%m/%Y %H:%M:%S')
                reloj.config(text=format)
                reloj.after(200, hora)

            reloj = Label(titulo, padx=100, pady=10, font=(
                'arial', 20, 'bold'), bg='gray20', fg='white')
            reloj.grid(row=0, column=3, sticky='w')
            hora()

            """------  SECCION BOTONES -------"""
            contenedor_1 = Frame(self.root2, bg="red3",
                                 borderwidth=4,  relief="ridge")
            contenedor_1.grid(row=1, column=0, padx=1)
            botones = Frame(contenedor_1, bg="gray20")
            botones.grid(row=0, column=0)

            Label(botones, text="Seleccione Proveedor:", padx=13, pady=10, font=(
                "arial", 18, "bold"), fg="white", bg="gray20").grid(row=0, column=0)

            """estilos para la lista del combobox"""
            botones.option_add("*TCombobox*Background", 'gray60')
            botones.option_add("*TCombobox*Font", "arial 18")
            botones.option_add("*TCombobox*selectBackground", "black")
            botones.option_add("*TCombobox*selectForeground", "orangered")
            botones.option_add("*TCombobox*Justify", "center")

            def update(data):
                """subo los datos al combobox"""
                combo_proveedores["values"] = data

            def check(e):
                """ chequea si esta el item"""
                typed = combo_proveedores.get()
                if typed == "":
                    data = self.nombres_proveedores()
                else:
                    data = []
                    for i in self.nombres_proveedores():
                        if typed.lower() in i.lower():
                            data.append(i)
                update(data)

            """ Defino el combobox"""
            combo_proveedores = ttk.Combobox(
                botones, width=25)
            combo_proveedores.grid(row=0, column=1, ipady=10, pady=1)

            update(self.nombres_proveedores())
            combo_proveedores.bind("<KeyRelease>", check)

            """Botones"""
            ttk.Button(botones, text="SELECCIONAR",
                       command=lambda: self.seleccionar(combo_proveedores, tree, e_comentario2, e_nombre, e_telefono, e_correo, e_direccion, e_comentario, titulo, btn_guardar_prov, guardar_proveedor, self.nombres_proveedores)).grid(row=0, column=2, padx=15, pady=10, sticky="we")
            ttk.Button(botones, text="EDITAR",
                       command=lambda: self.modificar(combo_proveedores, e_nombre, e_telefono, e_correo, e_direccion, e_comentario, titulo, btn_guardar_prov, tree, e_comentario2, self.nombres_proveedores, guardar_proveedor)).grid(row=0, column=3, padx=15, pady=10, sticky="we")
            ttk.Button(botones, text="BORRAR",
                       command=lambda: self.borrar(combo_proveedores, self.nombres_proveedores, tree, e_nombre, e_telefono, e_correo, e_direccion, e_comentario, e_comentario2, titulo, btn_guardar_prov, guardar_proveedor)).grid(row=0, column=4, padx=15, pady=10, sticky="we")

            """ ----- SECCION VISUALIZAR DATOS ------"""

            contenedor_2 = Frame(self.root2, bg="red3",
                                 borderwidth=4,  relief="ridge")
            contenedor_2.grid(row=2, column=0, pady=2)

            frame_tree = Frame(contenedor_2, bg="gray20")
            frame_tree.grid(row=0, column=0)
            columns2 = ('#0', '#1', '#2', '#4')
            tree = ttk.Treeview(frame_tree, columns=columns2,
                                show='headings', height=2)
            # el show='headings' oculta la columan 0 del arbol
            tree.column("#1", width=300, minwidth=30, anchor="center")
            tree.column("#2", width=200, minwidth=30, anchor="center")
            tree.column("#3", width=350, minwidth=30, anchor="center")
            tree.column("#4", width=350, minwidth=30, anchor="center")
            tree.heading('#1', text='Nombre', anchor="center")
            tree.heading('#2', text='Telefono', anchor="center")
            tree.heading('#3', text='Correo Electronico', anchor="center")
            tree.heading('#4', text='Direccion', anchor="center")

            tree.grid(row=0, column=0, columnspan=2)
            Label(frame_tree, text="Comentario:", bg="gray10", fg="orangered", font=(
                "arial", 18, 'bold'), bd=6).grid(row=2, column=0, sticky='we', padx=10, pady=5)
            e_comentario2 = Text(frame_tree, bg='pale goldenrod', font=(
                "arial", 15), width=52, height=2)
            e_comentario2.grid(row=2, column=1, sticky='w', padx=10, pady=5)

            """ ---- SECCION INGRESAR DATOS -----"""

            contenedor_3 = Frame(self.root2, bg="red3",
                                 borderwidth=4, relief="ridge")
            contenedor_3.grid(row=3, column=0)

            entradas = Frame(contenedor_3, bg="gray20")
            entradas.grid(row=0, column=0)
            titulo = Label(entradas, text="Ingresar un Nuevo Proveedor:", padx=10, pady=10, font=(
                "arial", 20, "bold"), bg="gray20", fg="white",)
            titulo.grid(row=0, column=0, columnspan=3, sticky='w')
            Label(entradas, text="Nombre:", bg="gray10", fg="orangered", font=(
                "arial", 15), bd=6, width=19).grid(row=1, column=0, sticky="we", padx=10, pady=5)
            Label(entradas, text="Telefono:", bg="gray10", fg="orangered", font=(
                "arial", 15), bd=6,).grid(row=2, column=0, sticky="we", padx=10, pady=5)
            Label(entradas, text="Correo Electronico:", bg="gray10", fg="orangered", font=(
                "arial", 15), bd=6, width=20).grid(row=1, column=2, sticky="we", padx=10, pady=5)
            Label(entradas, text="Direccion:", bg="gray10", fg="orangered", font=(
                "arial", 15), bd=6).grid(row=2, column=2, sticky="we", padx=10, pady=5)
            Label(entradas, text="Comentario:", bg="gray10", fg="orangered", font=(
                "arial", 15), bd=6).grid(row=3, column=0, sticky="we", padx=10, pady=5)

            e_nombre = Entry(entradas, bg='pale goldenrod',
                             font=("arial", 15, "bold"), width=30)
            e_nombre.grid(row=1, column=1, ipady=5, pady=5)

            e_telefono = Entry(entradas, bg='pale goldenrod',
                               font=("arial", 15, "bold"), width=30)
            e_telefono.grid(row=2, column=1, padx=10, ipady=5, pady=5)

            e_correo = Entry(entradas, bg='pale goldenrod',
                             font=("arial", 15, "bold"), width=30)
            e_correo.grid(row=1, column=3, padx=10, ipady=5, pady=5)

            e_direccion = Entry(entradas, bg='pale goldenrod',
                                font=("arial", 15, "bold"), width=30)
            e_direccion.grid(row=2, column=3, padx=10, ipady=5, pady=5)

            e_comentario = Text(entradas, bg='pale goldenrod', font=(
                "arial", 15, "bold"), width=52, height=2)
            e_comentario.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

            btn_guardar_prov = ttk.Button(
                entradas, text="GUARDAR PROVEEDOR", command=lambda: self.guardar(e_nombre, e_telefono, e_correo, e_direccion, e_comentario, combo_proveedores, self.nombres_proveedores))
            btn_guardar_prov.grid(row=3, column=3, pady=10)

        except:
            showerror(title="Error",
                      message="Surgio un error inesperado, contacte con el fabricante")

        ttk.Button(self.root2, text="C E R R A R    T O D O", style='Btn_cerrar.TButton', width=40,
                   command=self.root2.destroy).grid(row=4, column=0, pady=4)

        ttk.Button(self.root2, text='Limpiar todos los campos',
                   command=lambda: self.limpiar_todo(e_nombre, e_telefono, e_correo, e_direccion, e_comentario, tree, e_comentario2, combo_proveedores)).grid(row=4, column=0, padx=40, sticky='e')

        for i in range(0, 5):
            self.root2.rowconfigure(i, weight=1)
            titulo.rowconfigure(i, weight=1)
            contenedor_1.rowconfigure(i, weight=1)
            contenedor_2.rowconfigure(i, weight=1)
            contenedor_3.rowconfigure(i, weight=1)
            frame_tree.rowconfigure(i, weight=1)
            botones.rowconfigure(i, weight=1)
            entradas.rowconfigure(i, weight=1)

        for i in range(0, 4):
            self.root2.columnconfigure(i, weight=1)
            titulo.columnconfigure(i, weight=1)
            contenedor_1.columnconfigure(i, weight=1)
            contenedor_2.columnconfigure(i, weight=1)
            contenedor_3.columnconfigure(i, weight=1)
            frame_tree.columnconfigure(i, weight=1)
            botones.columnconfigure(i, weight=1)
            entradas.columnconfigure(i, weight=1)

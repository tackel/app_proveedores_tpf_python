
from tkinter import ttk


class Estilos:
    """Clase que contiene los estilos utilizados"""

    def estilos_combos(self):
        estilo = ttk.Style()
        estilo.theme_use('alt')
        estilo.configure('TCombobox', background='gray40', borderwidth=200, fieldbackground='gray10',
                         selectbackground='gray10', foreground='orangered', selectforeground='orangered')
        estilo.map('TCombobox', fieldbackground=[('readonly', 'gray10')])

    def estilo_botones(self):
        est_boton = ttk.Style()
        est_boton.theme_use('alt')
        est_boton.configure("TButton", background='gray40', padding=10, borderwidth=4,
                            foreground='black', font=("arial", 15, "bold"), relief="ridge", justify='center')
        est_boton.map("TButton", background=[('active', 'black')])
        est_boton.map("TButton", foreground=[('active', 'orangered')])

    def estilo_btn_cerrar(self):

        est_boton2 = ttk.Style()
        est_boton2.theme_use('alt')
        est_boton2.configure("Btn_cerrar.TButton", background='red3', padding=10, borderwidth=5,
                             foreground='white', font=("arial", 15, "bold"), justify='center')
        est_boton2.map("Btn_cerrar.TButton", background=[('active', 'gray10')])
        est_boton2.map("Btn_cerrar.TButton", foreground=[('active', 'red')])

    def estilo_tree(self):
        style = ttk.Style()
        style.theme_use('alt')
        style.configure("Treeview", background="pale goldenrod",
                        fieldbackground="gray20", rowheight=30, font=('arial', 13))
        style.configure("Treeview.Heading", background='gray10',
                        foreground='orangered', font=('arial', 18, 'bold'))
        style.map("Treeview", background=[('selected', 'orangered')])

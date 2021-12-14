from tkinter import Tk
from vistas import Vistas_app_proveedores
from base_datos.base_datos import *

"""Este es el controlador donde esta la clase que envia a el root a la ventana general
Por aca se ejecuta la aplicacion."""


class Mi_app:

    def __init__(self, window):
        self.ventana = window
        Vistas_app_proveedores(self.ventana)


if __name__ == "__main__":
    root2 = Tk()
    objeto = Mi_app(root2)
    root2.mainloop()

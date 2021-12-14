
from tkinter.constants import END
from tkinter.messagebox import showerror, showinfo
from modificar.modificar import modificar_proveedor
from guardar.guardar import guardar_proveedor
from mostrar.mostrar import mostrar_provedor
from borrar.borrar import borrar_proveedor

from base_datos.base_datos import *
import subprocess
import sys
import threading
import time
import os
from pathlib import Path

theproc = ""


class Servidor():
    """ Clase que maneja el servidor """

    def activa_server():
        """ Activa el server """
        print('Espere 3 segudnos')
        if theproc != "":
            theproc.kill()
            threading.Thread(target=Servidor.lanzar_servidor, args=(
                True,), daemon=True).start()
            time.sleep(3)
            print('Servidor Activado')
            showinfo(title="Info",
                     message="Servidor Activado")
        else:
            threading.Thread(target=Servidor.lanzar_servidor, args=(
                True,), daemon=True).start()
            time.sleep(3)
            showinfo(title="Info",
                     message="Servidor Activado")

    def stop_server():
        """ Detiene el server """

        global theproc
        if theproc != "":
            theproc.kill()
            print('Servidor Detenido')
            showinfo(title="Info",
                     message="Servidor Detenido")

    def lanzar_servidor(args):
        raiz = Path(__file__).resolve().parent
        ruta_server = os.path.join(raiz, 'udp_server_t.py')
        the_path = ruta_server
        if args == True:
            global theproc
            theproc = subprocess.Popen([sys.executable, the_path])
            theproc.communicate()

        else:
            print("")


class Funciones_abmc():
    """Clase que contiene el CRUD para la seccion de proveedores con ORM"""

    def nombres_proveedores(self):
        """Funcion que retorna unicamente el nombre de los proveedores guardados"""
        try:
            nombres_prov = []
            for i in Proveedores.select():
                nombres_prov.append(i.nombre)
            return nombres_prov
        except:
            showerror(title="Error",
                      message="Error fatal con este registro mostrar")

    def limpiar_todo(self, e_nombre, e_telefono, e_correo, e_direccion, e_comentario, tree, e_comentario2, combo_proveedores):
        """Funcion que limpia de datos los entry, tree, combobox, y cuadro de texto"""
        e_nombre.delete("0", END)
        e_telefono.delete("0", END)
        e_correo.delete("0", END)
        e_direccion.delete("0", END)
        e_comentario.delete("1.0", END)
        for i in tree.get_children():
            tree.delete(i)
        e_comentario2.delete('1.0', END)
        combo_proveedores.delete('0', END)

    def guardar(self, *args):
        """Funcion que llama al modulo guardar"""
        guardar_proveedor(*args)

    def seleccionar(self, *args):
        """Funcion que llama al modulo mostrar"""
        mostrar_provedor(*args)

    def borrar(self, *args):
        """Funcion que llama al modulo borrar"""
        borrar_proveedor(*args)

    def modificar(self, *args):
        """Funcion que llama al modulo modificar"""
        modificar_proveedor(*args)

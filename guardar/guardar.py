
import re
from sqlite3.dbapi2 import Error
from tkinter.constants import END
from tkinter.messagebox import showerror, showinfo
from base_datos.base_datos import *
from deco.decoradores import *

"""Funcion para guardar proveedor ingresado por medio de orm"""


@decorador_crud('Alta')
def guardar_proveedor(e_nombre, e_telefono, e_correo, e_direccion, e_comentario, combo_proveedores, nombres_proveedores):

    try:
        if e_nombre.get() != "":
            nombre = e_nombre.get()
            telefono = e_telefono.get()
            correo = e_correo.get()
            direccion = e_direccion.get()
            comentarios = e_comentario.get("1.0", "end")
            """Patron para validar el nombre ingresado para que sea alfa numerico"""
            patron = '^[a-z0-9_.-]+@[a-z0-9._-]+\.[a-z]{2,}$'
            # mira si hay algo escrito en correo electronico para validarlo
            if correo != '':
                if re.match(patron, correo):
                    validar = True
                else:
                    validar = False
            else:
                validar = True

            if validar == True:
                try:
                    prov = Proveedores()
                    prov.nombre = nombre
                    prov.telefono = telefono
                    prov.correo_electronico = correo
                    prov.direccion = direccion
                    prov.comentarios = comentarios
                    prov.save()
                    # mostrar_orm()
                    showinfo(
                        title="Agregar Proveedor",
                        message=f"Proveedor, { nombre }, GUARDADO con exito", )
                    e_nombre.delete("0", END)
                    e_telefono.delete("0", END)
                    e_correo.delete("0", END)
                    e_direccion.delete("0", END)
                    e_comentario.delete("1.0", END)
                except Error as e:
                    print(e)
                    showerror(title="Error",
                              message="Error fatal con este registro guardar")
            else:
                showerror(title='Error',
                          message='Formato de direccion de correo incorrecta')
        else:
            showerror(
                title="Error",
                message="El campo Nombre no puede estar VACIO, intentelo nuevamente",
            )
        combo_proveedores["values"] = nombres_proveedores()
    except Error as e:
        print(e)
        showerror(title="Error", message="Este Proveedor ya EXISTE, los nombres no pueden repetirse",
                  )

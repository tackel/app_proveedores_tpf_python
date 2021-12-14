
from tkinter.constants import END
from tkinter.messagebox import showerror
from base_datos.base_datos import *
from deco.decoradores import *


@decorador_mostrar('Consulta')
def mostrar_provedor(combo_proveedores, tree, e_comentario2, e_nombre, e_telefono, e_correo, e_direccion, e_comentario, titulo, btn_guardar_prov, guardar_proveedor, nombres_proveedores):
    """Funcion para mostrar datos de proveedor ya existente con orm"""
    proveedor = combo_proveedores.get()
    try:
        for i in Proveedores.select():

            if i.nombre == proveedor:
                provee = []
                provee2 = []
                coment = ''

                provee.append(
                    (i.nombre, i.telefono, i.correo_electronico, i.direccion))
                coment = i.comentarios
                provee2.append(
                    (i.nombre, i.telefono, i.correo_electronico, i.direccion, i.comentarios))
                for i in tree.get_children():
                    tree.delete(i)
                for i in provee:
                    tree.insert("", END, values=i)
                e_comentario2.delete('1.0', END)
                e_comentario2.insert(END, coment)

                e_nombre.delete("0", END)
                e_telefono.delete("0", END)
                e_correo.delete("0", END)
                e_direccion.delete("0", END)
                e_comentario.delete("1.0", END)
                titulo.config(text="Ingresar un Nuevo Proveedor:")
                btn_guardar_prov.config(text="GUARDAR PROVEEDOR",
                                        command=lambda: guardar_proveedor(e_nombre, e_telefono, e_correo, e_direccion, e_comentario, combo_proveedores, nombres_proveedores))

        return provee2
    except:
        showerror(title="Error", message="El Nombre buscado no existe.")

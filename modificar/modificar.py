from tkinter.constants import END
from tkinter.messagebox import showerror, showinfo
import re
from base_datos.base_datos import *
from deco.decoradores import *


def modificar_proveedor(combo_proveedores, e_nombre, e_telefono, e_correo, e_direccion, e_comentario, titulo, btn_guardar_prov, tree, e_comentario2, nombres_proveedores, guardar_proveedor):
    """ Modifica los datos de un proveedor, y los guarda. Con orm """
    buscar = combo_proveedores.get()
    if buscar == "":
        showerror(title="Error", message="No se selecciono proveedor")
        combo_proveedores.focus()
    else:
        try:
            for i in Proveedores.select():
                if i.nombre == buscar:
                    id_nombre = i.id
                    e_nombre.delete("0", END)
                    e_nombre.insert(0, i.nombre)
                    e_telefono.delete("0", END)
                    e_telefono.insert(0, i.telefono)
                    e_correo.delete("0", END)
                    e_correo.insert(0, i.correo_electronico)
                    e_direccion.delete("0", END)
                    e_direccion.insert(0, i.direccion)
                    e_comentario.delete("1.0", END)
                    e_comentario.insert(END, i.comentarios)
                titulo.config(
                    text=f'Modifique los Datos de {buscar} y Precione GUARDAR ')
                btn_guardar_prov.config(text="Guardar Cambios",
                                        command=lambda: guardar_cambios())
                for i in tree.get_children():
                    tree.delete(i)
                e_comentario2.delete("1.0", END)

        except Error as e:
            print(e)
            showerror(title="Error", message="El Nombre buscado no existe.")


# -------------------------- GUARDAR CAMBIOS MODIFICADOS ----------------------

    @decorador_crud('Modificacion')
    def guardar_cambios():
        """Funcion para guardar cambios en proveedores ya existentes"""
        try:
            nombre = e_nombre.get()
            telefono = e_telefono.get()
            correo = e_correo.get()
            direccion = e_direccion.get()
            comentario = e_comentario.get("1.0", "end")
            """Patron de validacion alfa numerico"""
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
                    modifica = Proveedores.update(
                        nombre=nombre,
                        telefono=telefono,
                        correo_electronico=correo,
                        direccion=direccion,
                        comentarios=comentario).where(Proveedores.id == id_nombre)
                    modifica.execute()
                    showinfo(
                        title="CAMBIO DE DATOS",
                        message=f"Proveedor, { nombre }, GUARDADO con exito",
                    )
                    titulo.config(text="Ingresar un Nuevo Proveedor:")
                    btn_guardar_prov.config(text="GUARDAR PROVEEDOR",
                                            command=lambda: guardar_proveedor(e_nombre, e_telefono, e_correo, e_direccion, e_comentario, combo_proveedores, nombres_proveedores))
                    e_nombre.delete("0", END)
                    e_telefono.delete("0", END)
                    e_correo.delete("0", END)
                    e_direccion.delete("0", END)
                    e_comentario.delete("1.0", END)

                    combo_proveedores["values"] = nombres_proveedores()
                    combo_proveedores.delete('0', END)

                except:
                    showerror(
                        title="Error", message="Error fatal con este registro modificar")
            else:
                showerror(title='Error',
                          message='Formato de direccion de correo incorrecta')
        except:
            showerror(
                title="Error",
                message=f"El nombre {nombre} ya existe, intente eligiendo otro nombre",
            )

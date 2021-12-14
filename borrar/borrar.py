from deco.decoradores import *
from tkinter.constants import END
from tkinter.messagebox import askquestion, showinfo, showerror
from base_datos.base_datos import *


@decorador_crud('borrado')
def borrar_proveedor(combo_proveedores, nombres_proveedores, tree, e_nombre, e_telefono, e_correo, e_direccion, e_comentario, e_comentario2, titulo, btn_guardar_prov, guardar_proveedor):
    """funcion que borra el proveedor selccionado con orm"""
    borrar = combo_proveedores.get()
    if borrar != "":
        respuesta = askquestion(
            title="Confirmar", message=f"Seguro de querer BORRAR a {borrar}?"
        )
        if respuesta == "yes":
            try:
                borrar = Proveedores.get(Proveedores.nombre == borrar)
                borrar.delete_instance()
                showinfo(
                    title="Confirmado",
                    message=f"Proveedor BORRADO con exito.",
                )
                combo_proveedores["values"] = nombres_proveedores()
                for i in tree.get_children():
                    tree.delete(i)
                combo_proveedores.delete('0', END)
                e_nombre.delete("0", END)
                e_telefono.delete("0", END)
                e_correo.delete("0", END)
                e_direccion.delete("0", END)
                e_comentario.delete("1.0", END)
                e_comentario2.delete("1.0", END)
                titulo.config(text="Ingresar un Nuevo Proveedor:")
                btn_guardar_prov.config(text="GUARDAR PROVEEDOR",
                                        command=lambda: guardar_proveedor(e_nombre, e_telefono, e_correo, e_direccion, e_comentario, combo_proveedores, nombres_proveedores))

            except:
                showerror(title="Error",
                          message="Error fatal con este registro eliminar")
    else:
        showerror(title="Error", message="Debe Seleccionar un Nombre")

from sqlite3.dbapi2 import Error
from tkinter.messagebox import showerror
from peewee import *

"""Creao la base de datos y la tabla por medio de orm"""

try:
    bd = SqliteDatabase("./base_datos/base_datos_orm.db")

    class Mi_base_de_datos(Model):
        class Meta:
            database = bd

    class Proveedores(Mi_base_de_datos):
        id = IntegerField(primary_key=True)
        nombre = CharField(null=False, unique=True)
        telefono = CharField()
        correo_electronico = CharField()
        direccion = CharField()
        comentarios = TextField()

    class Registro(Mi_base_de_datos):
        id = IntegerField(primary_key=True)
        hora = CharField(null=False)
        observacion = TextField()

    bd.connect()
    bd.create_tables([Proveedores, Registro])
except Error as e:
    showerror(title="Error",
              message=f"Surgio un error el crear las tablas: {e} ")

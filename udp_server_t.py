import socketserver
import binascii
from datetime import datetime
import datetime
from base_datos.base_datos import *


global PORT


"""Decorador que observa al server para hacer su trabajo"""


def deco_server(funcion):
    def _observador(*args):
        dato_recibido = funcion(*args)
        """Registro de log """
        now = datetime.datetime.now()
        now_ya = now.strftime("%d/%m/%Y - %H:%M:%S")
        log = open('./log.txt', 'a')
        print(now_ya, 'Un cliente consulto los datos del proveedor: ',
              dato_recibido, file=log)

        """ Registro en base de datos"""
        dato = f'Un cliente consulto los datos del proveedor: {dato_recibido} '
        registro = Registro()
        registro.hora = now_ya
        registro.observacion = dato
        registro.save()
    return _observador


class MyUDPHandler(socketserver.BaseRequestHandler):
    @deco_server
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        try:
            """Recibo los datos del cliente"""
            dato_recibido = data.decode('UTF-8')
            dato_recibido = dato_recibido.upper()
            global provee2
            provee2 = ''
            all_nom = []
            """ busca los datos en la base de datos"""
            for i in Proveedores.select():
                nom = i.nombre.upper()
                all_nom.append(i.nombre.upper())
                if nom == dato_recibido:
                    provee2 = f'Datos solicitados:{i.nombre}, Tel: {i.telefono},Corro: {i.correo_electronico} , Direccion: {i.direccion}, Comentario: {i.comentarios}'
            if provee2 == '':
                provee2 = f'No existe el proveedor. Las opciones son: {all_nom}'
            mensaje = provee2
            """Envio de datos al cliente"""
            packed_data_2 = mensaje.encode("UTF-8")
            socket.sendto(packed_data_2, self.client_address)
            print(packed_data_2)
            return dato_recibido

        except:
            """ Recive datos del cliente en hexa"""
            binary_field = bytearray(data)
            dato_recivido2 = binascii.hexlify(
                binary_field).decode("utf-8")
            print("Valor recibido: ", binascii.hexlify(
                binary_field).decode("utf-8"))
            value2 = 0xA0
            """Envia respuesta al cliente"""
            packed_data_2 = bytearray()
            packed_data_2 += value2.to_bytes(1, "big")
            socket.sendto(packed_data_2, self.client_address)
            print('respuesta:', (packed_data_2))
            return dato_recivido2


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()

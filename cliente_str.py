import socket
import sys


HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

""" Mensaje a enviar, puede cambiarse o poner un nombre que no exista para ver el mensaje de respeusta"""
mensaje = "coca cola"
print('Mensaje enviado:', mensaje)
# Se envia el mensaje
sock.sendto(mensaje.encode("UTF-8"), (HOST, PORT))
# se recive la respuesta
received = sock.recvfrom(1024)
print(received[0].decode("utf-8"))


# ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================

import datetime

""" Decoradores del crud"""


def decorador_crud(variable):
    def _decorador_crud(funcion):
        def aviso(*args):
            now = datetime.datetime.now()
            now = now.strftime("%d/%m/%Y - %H:%M:%S")
            funcion(*args)

            log = open('./log.txt', 'a')
            # Envio de mensaje a archivo txt
            print(
                f'{now}. Accion realizada: {variable} de registro. Lo sabes gracias a un decorador.', file=log)
        return aviso
    return _decorador_crud


def decorador_mostrar(variable):
    def _decorador_mostrar(funcion):
        def observador(*args):
            now = datetime.datetime.now()
            now = now.strftime("%d/%m/%Y - %H:%M:%S")
            funcion(*args)
            lista = funcion(*args)
            log = open('./log.txt', 'a')
            # Envio de mensaje a archivo txt
            print(
                f'{now}. Accion: {variable} de registro. Nombre: {lista[0][0]}, Tel: {lista[0][1]}, Correo: {lista[0][2]} ,Direccion: {lista[0][3]}, Comentario: {lista[0][4]}', file=log)
        return observador
    return _decorador_mostrar

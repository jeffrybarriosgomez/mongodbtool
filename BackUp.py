import os
from sys import platform


def backup():
    ip = input('Digite IP de la base de datos:[127.0.0.1] ')
    port = input('Digite puerto de mongo:[27017] ')
    db = input('Digite nombre de la base de datos: ')
    user = input('Digite nombre de USUARIO de la DB mongo: ')
    pw = input('Digite CONTRASEÑA del usuario de la DB mongo: ')
    dir_out = input('Ingrese ruta para guardar la base de datos: ')
    if ip == "":
        ip = "127.0.0.1"
    if port == "":
        port = "27017"

    path = os.path.dirname(os.path.realpath(__file__))

    if user == "" or pw == "":
        dump = f"{path}/bin/{os_name()}/mongodump --host {ip} --port {port} -d {db} --out {dir_out}"
    else:
        dump = f"{path}/bin/{os_name()}/mongodump --host {ip} --port {port} -d {db} --out {dir_out} --authenticationDatabase admin --authenticationMechanism SCRAM-SHA-1 --username {user} --password {pw}"
    os.system(dump)
    print('BackUp creado con exito')


def restored():
    ip = input('Digite IP de la base de datos:[127.0.0.1] ')
    port = input('Digite puerto de mongo:[27017] ')
    db = input('Digite nombre de la base de datos con el que va restaurar: ')
    user = input('Digite nombre de USUARIO de la DB mongo: ')
    pw = input('Digite CONTRASEÑA del usuario de la DB mongo: ')
    dir_out = input('Ingrese ruta de la copia guardada de la base de datos: ')
    if ip == "":
        ip = "127.0.0.1"
    if port == "":
        port = "27017"

    path = os.path.dirname(os.path.realpath(__file__))
    insert = f"{path}/bin/{os_name()}/mongosh {ip}:{port}/{db} {path}/entity.js"
    os.system(insert)
    if user == "" or pw == "":
        dump = f"{path}/bin/{os_name()}/mongorestore --host {ip} --port {port} -d {db} --drop {dir_out}"
    else:
        dump = f"{path}/bin/{os_name()}/mongorestore --host {ip} --port {port} -d {db} --drop {dir_out} --authenticationDatabase admin --authenticationMechanism SCRAM-SHA-1 --username {user} --password {pw}"
    os.system(dump)
    print('BackUp restaurado con exito')


def os_name():
    sistema = ''
    if platform == 'win32':
        sistema = 'windows'
    elif platform == "linux" or platform == "linux2":
        sistema = 'linux'

    return sistema


if __name__ == "__main__":
    sw = 0
    while sw == 0:
        print('1. Crear Backup')
        print('2. Restaurar Backup')
        print('3. Salir\n')
        print('Escoger una opción: ')

        option = int(input())

        if option == 1:
            backup()
            sw = 1
        elif option == 2:
            restored()
            sw = 1
        elif option == 3:
            exit()
        else:
            print('Opcion invalida')
            sw = 0

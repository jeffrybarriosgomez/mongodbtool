import os
from sys import platform


def backup():
  try:
    ip = input('Enter the database IP [127.0.0.1]: ') or "127.0.0.1"
    port = input('Enter the MongoDB port [27017]: ') or "27017"
    db_name = input('Enter the database name: ')
    user = input('Enter the MongoDB user: ')
    password = input('Enter the MongoDB user password: ')
    backup_dir = input('Enter the backup directory path: ')

    path = os.path.dirname(os.path.realpath(__file__))
    dump_command = f"{path}/bin/{os_name}/mongodump --host {ip} --port {port} -d {db_name} --out {backup_dir}"

    if user and password:
      dump_command += f" --authenticationDatabase admin --authenticationMechanism SCRAM-SHA-1 --username {user} --password {password}"
    os.system(dump_command)
    print('BackUp creado con exito')
  except Exception as e:
    print(f"Error al crea BackUp {e}")


def restore():
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

def main():
  while True:
    print('1. Create Backup')
    print('2. Restore Backup')
    print('3. Exit\n')
    
    try:
      option = int(input('Choose an option: '))
    except ValueError:
      print('Invalid option. Please try again.')
      continue
    if option == 1:
      backup()
      break
    elif option == 2:
      restore()
      break
    elif option == 3:
      print('Exiting...')
      break
    else:
      print('Invalid option. Please try again.')

if __name__ == "__main__":
  main()
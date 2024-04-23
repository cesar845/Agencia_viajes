list_viajeros = []
import os
sw = True
def fnt_limpiar():
    os.system("cls")
    print('Autor: Cesar A. Castro')
    print('Copyright(c) 2024')
    print('Universidad Catolica Luis Amigo\n')

def fnt_agente(op):
    global sw
    fnt_limpiar()
    if op == '1':
        print(' >>> Agregar viajero <<< ')
        viajero = ''
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        edad = input('Edad: ')
        if (int(edad) > 0 and int(edad) <= 25):
            viajero = nombre + ' ' + apellido + ' ' + edad
            list_viajeros.append(viajero)
            print('Viajero agregado correctamente\n')
            input('Presione <ENTER> para continuar...')
        else:
            print('\nEdad invalida\n')
            input('Presione <ENTER> para continuar...')
    elif op == '2':
        fnt_limpiar()
        print(' >>> Mostrar viajeros <<< ')
        if len(list_viajeros) == 0:
            print('No hay viajeros registrados\n')
            input('Presione <ENTER> para continuar...')
        else:
            for i in range(len(list_viajeros)):
                print(list_viajeros[i])
            input('Presione <ENTER> para continuar...')
    elif op == '3':
        sw = False

while sw == True:
    fnt_limpiar()
    opcion = input('  <<<<  MENU PRINCIPAL  >>>>  \n1. Agregar\n2. Mostrar\n3. Salir\n4 -> ')
    fnt_agente(opcion)
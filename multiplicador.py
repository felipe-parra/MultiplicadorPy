#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import os
import sys

def ahora_fecha():
    fecha = time.strftime("%Y-%m-%dT%X %Z")
    return fecha


def cleaning():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


def nombre_archivo():
    fecha = time.strftime("%Y-%m-%d_%H%M")
    nombre = "Resultado %s.txt" % (fecha)
    return nombre


billetes = [1000, 500, 200, 100, 50, 20]
decorador_str = "*"*80

cleaning()

def decorador():
    print('*' * 110)

def nombre():
    print(" ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗ ")
    print("██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗")
    print("██║     ███████║██║     ██║     ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║")
    print("██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║")
    print("╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║")
    print(" ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝")
    print("                                                                                          ")

decorador_resultado = '''
██████╗ ███████╗███████╗██╗   ██╗██╗     ████████╗ █████╗ ██████╗  ██████╗
██╔══██╗██╔════╝██╔════╝██║   ██║██║     ╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗
██████╔╝█████╗  ███████╗██║   ██║██║        ██║   ███████║██║  ██║██║   ██║
██╔══██╗██╔══╝  ╚════██║██║   ██║██║        ██║   ██╔══██║██║  ██║██║   ██║
██║  ██║███████╗███████║╚██████╔╝███████╗   ██║   ██║  ██║██████╔╝╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝
'''

def decorador_resultado():
    print("██████╗ ███████╗███████╗██╗   ██╗██╗     ████████╗ █████╗ ██████╗  ██████╗ ")
    print("██╔══██╗██╔════╝██╔════╝██║   ██║██║     ╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗")
    print("██████╔╝█████╗  ███████╗██║   ██║██║        ██║   ███████║██║  ██║██║   ██║")
    print("██╔══██╗██╔══╝  ╚════██║██║   ██║██║        ██║   ██╔══██║██║  ██║██║   ██║")
    print("██║  ██║███████╗███████║╚██████╔╝███████╗   ██║   ██║  ██║██████╔╝╚██████╔╝")
    print("╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝ ")
    print("                                                                           ")

def main():
    decorador()
    nombre()
    decorador()
    #print('\t\t\tMultiplicador')
    decorador()
    mil = 0
    qui = 0
    dos = 0
    cie = 0
    cin = 0
    vei = 0

    m_mil = 0
    m_qui = 0
    m_dos = 0
    m_cie = 0
    m_cin = 0
    m_vei = 0

    cantidades = [mil, qui, dos, cie,cin, vei]
    multiplicados = [m_mil,m_qui ,m_dos, m_cie, m_cin, m_vei]

    for i in range(0,6):
        cantidades[i] = input('\nCantidad de Billetes de {}:\t'.format(billetes[i]))
        if cantidades[i] == '':
                multiplicados[i] = 0
                cantidades[i] = 0
        else:
            multiplicados[i] = int(cantidades[i]) * int(billetes[i])

    cleaning()
    decorador()
    decorador()
    print(decorador_resultado())
    print("\t\t" + ahora_fecha())
    decorador()
    print('\tBillete\t\tCantidad\tImporte')
    decorador()
    for i in range(0,6):
        print('\t{:,} \tx \t{}\t:\t{:,}'.format(billetes[i], cantidades[i], multiplicados[i]))
    decorador()
    suma = 0
    for i in range(0,6):
        suma += multiplicados[i]

    print('********\tSuma Total:\t$\t{:,}\t\t\t\t********'.format(suma))
    decorador()
    escribiendo_en_archivo('resultados.txt',ahora_fecha(),cantidades,multiplicados,suma)


def escribiendo_en_archivo(nombre_archivo,fecha,cantidades,importes,total):
    fichero_csv = open(nombre_archivo, 'a')
    fichero_csv.write(fecha[0:19] + ', ')
    for i in range(0,6):
        fichero_csv.write('{}, '.format(cantidades[i]))
    fichero_csv.write('${:,}'.format(total))
    fichero_csv.write('\n')
    fichero_csv.close()


if __name__ == '__main__':
    main()
    while True:
        selection_command = input("Quieres realizar otra operacion? y/n\t")
        if selection_command == '' or selection_command.lower() == 'n' or selection_command.upper() == 'no':
            break
        else:
            cleaning()
            main()

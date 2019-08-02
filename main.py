#Evil SoFiA
import re
import time 
import sys
import os
from random import randint
version = ' 1.9.1'
time.sleep(0.5)
execute = os.system

def correctRead(number, bin):
    read = 0
    while True:
        try:
            read = (input('  Introduce el dígito número ' + number + ' del ' + bin + ' Bin: '))
            if read >= 0 and read <= 9:
                break
            else:
                print('   Valor inválido')
        except Exception:
            print('   UN NUMERO')
    return read

def extrapolador():
    execute('title Extrapolador')
    execute('cls')
    execute('color 3')
    time.sleep(1.5)
    print("\tACCESS GRANTED!")
    time.sleep(1.5)
    print("")
    bin = (input("  Digite los primeros 8 digitos del Bin: "))
    lista = []
    lista.append(bin)
    # Primer Bin
    bin11 = correctRead('DIEZ', 'primer')
    bin12 = correctRead('ONCE', 'primer')
    # Segundo Bin
    bin21 = correctRead('DIEZ', 'segundo')
    bin22 = correctRead('ONCE', 'segundo')
    # Algoritmo
    a = int(bin11 + bin21 / 2) * 5
    b = int(bin12 + bin22 / 2) * 5
    c = a + b
    # Agregar los digitos
    lista.append(c)
    print("  Tu extrapolacion es: ")
    time.sleep(0.8)
    print("".join(repr(e) for e in lista))
    print("")
    time.sleep(2)
    raw_input("  Presiona Enter Para Salir De El Extrapolador")

def dniGenerator():
    #LAST DNI GEN
    execute("title LAST")
    execute("color 2")
    execute("cls")
    print time.strftime("               %I:%M:%S")
    print'''

    $$\        $$$$$$\   $$$$$$\ $$$$$$$$\ 
    $$ |      $$  __$$\ $$  __$$\\__$$  __|
    $$ |      $$ /  $$ |$$ /  \__|  $$ |   
    $$ |      $$$$$$$$ |\$$$$$$\    $$ |   
    $$ |      $$  __$$ | \____$$\   $$ |   
    $$ |      $$ |  $$ |$$\   $$ |  $$ |   
    $$$$$$$$\ $$ |  $$ |\$$$$$$  |  $$ |   
    \________|\__|  \__| \______/   \__|   


    '''
    dni=range(1,9)
    print("   Emmanuel Milos|Emilio Barroso|Joshua Salcido")
    i=0
    for element in dni:
        element=randint(1,9)
    dni2=''.join(map(str,dni))
    print ' '
    time.sleep(2)
    print ("          Generando DNI...")
    time.sleep(3)
    print '''
    '''
    numero = dni2
    intnumero = int(numero)
    letra1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resto = intnumero%23
    letra = letra1[resto]
    print '   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
    print '   %        ' + numero,  "-", letra + '       %'
    print'   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
    print " "
    raw_input("  Presiona Enter Para Salir De El Generador")
    print("")

def bye():
    print ("Gracias por Utlizar SoFiA")
    exit()

def defaul():
    print('En Construcción!')
    exit()
ols = time.strftime("%H:%M:%S")
print time.strftime("                     %I:%M:%S") 
if ols > "23:30":
    print "EVIL SOFIA SE ESTA ACTUALIZANDO!..."
    exit()
execute("color 4")
print '''
___ _   _  _ _      __   __  ___ _  __   
| __| \ / || | |   /' _/ /__\| __| |/  \  
| _|`\ V /'| | |_  `._`.| \/ | _|| | /\ | 
|___| \_/  |_|___| |___/ \__/|_| |_|_||_|  
'''
time.sleep(1.4)
execute("title EVIL SOFIA")
print "         Emmanuel Milos|Emilio Barroso|Joshua Salcido"
print "         ~EXTRAPOLADOR Y GENERADOR SOFIA~" 
print '''

'''

while True:
    execute("color 4")
    execute('cls')
    print("      .:MENU:.")
    print("   1.EXTRAPOLADOR")
    print("   2.GENERADOR DE DNI")
    print("   3.SALIR")
    print("")
    option = input("  Digite el numero de la optionion: ")
    print("")
    switcher = {
        1: extrapolador,
        2: dniGenerator,
        3: bye
    }
    func = switcher.get(option, exit)
    func()


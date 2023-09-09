#!/usr/bin/env python3
#craeted by Hans saldias
from random import randint as pasword
from time import sleep as ok
import os as killer
from colorama import init, Fore, Style, Back
init()
def four():
    killer.system("clear")
    title = """
    =====================================
    || password unlock phone 4 digit   ||
    ||                                 ||  
    || Created by: 1LugarParaProgramar ||
    ||                                 ||
    || Author : Hans saldias           ||
    =====================================             

\n\n"""
    for i in title:
        print(i, end="", flush=True)
        ok(0.1)
    integer = int(input("cuantas claves de 4 digitos desea generar: "))
    cont = 0
    
    while True:
        pw = pasword(0000,9999)
        print(pw,flush=True)
        ok(0.1)
        cont += 1
        with open("4digit.txt", 'a') as con:
            con.write(f"{pw}\n")
        if cont == integer:
           print("claves guardas exitosamente!! => 4digit.txt\n\n")
           break
        
def six():
    killer.system("clear")
    title2 = """
    =====================================
    || password unlock phone 6 digit   ||
    ||                                 ||  
    || Created by: 1LugarParaProgramar ||
    ||                                 ||
    || Author : Hans saldias           ||
    =====================================             

\n\n"""
    for i in title2:
        print(i, end="", flush=True)
        ok(0.1)
    integer = int(input("Cuantas claves de 6 digitos desea generar: "))
    cont = 0
    
    while True:
        pwd = pasword(000000,999999)
        print(pwd,flush=True)
        ok(0.1)
        cont += 1
        with open("6digit.txt", 'a') as con:
            con.write(f"{pwd}\n")
        if cont == integer:
            print("claves guardas exitosamente!! => 6digit.txt\n\n")
            break
           
def look():
    killer.system("clear")
    l = """
    =====================================
    ||       Look archive.txt          ||
    ||             saved               ||
    ||                                 || 
    || Created by: 1LugarParaProgramar ||
    ||                                 ||
    ||      Author : Hans saldias      ||
    ||                                 ||
    ||         ***  MENU ***           ||
    ||                                 ||
    ||  1 - Look  password 4 digit     ||
    ||                                 ||
    ||  2 - Look  password 6 digit     ||
    ||                                 ||
    ||  00 -        exit               ||
    =====================================             

\n\n"""
    for i in l:
        print(i, end="", flush=True)
        ok(0.1)
    try:
        op = int(input("insert options: "))
        if op == 1:
            killer.system("ls")
            ok(2)
            killer.system("cat 4digit.txt")
        elif op == 2:
            killer.system("ls")
            ok(2)
            killer.system("cat 6digit.txt")
        else:
            print("optins no found")
    except ValueError:
        print("options no found, insert option correct")
    input("press (enter)")





if __name__ == "__main__":
    while True:
        killer.system("clear")
        t = Fore.LIGHTGREEN_EX+Style.BRIGHT+"""
    =====================================
    ||       password unlock phone     ||
    ||                                 ||  
    || Created by: 1LugarParaProgramar ||
    ||                                 ||
    ||      Author : Hans saldias      ||
    ||                                 ||
    ||         ***  MENU ***           ||
    ||                                 ||
    ||  1 - Creat password 4 digit     ||
    ||                                 ||
    ||  2 - Creat password 6 digit     ||
    ||                                 ||
    ||  3 - look archive.txt password  ||
    ||                                 ||
    ||  00 -        exit               ||
    =====================================             

\n\n"""
        for i in t:
            print(i, end="", flush=True)
            ok(0.1)
        try:
            op = int(input("Insert options: "))
            if op == 1:
                four()
            elif op == 2:
                six()
            elif op ==3:
                look()
            elif op == 00:
                print("gracias por usar mi script: Hans saldias")
                break
            else:
                print("options no found")
        except ValueError:
            print("options no found, insert options correct")    
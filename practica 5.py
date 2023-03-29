# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:09:16 2023

@author: luis mercado
"""

def First_fit(n, proceso, mem_req, tam_bloq):
    Order = [None] * n
    flag = [False] * n 
    flag1 = [False] * n
    for i in range(len(mem_req)):
        for j in range(len(mem_req)):
            if (mem_req[i] <= tam_bloq[j] and flag[i] == False and flag1[j] == False):
                flag[i] = True
                flag1[j] = True
                Order[i] = j
    print()
    print("primer ajuste \n")
    print("proceso  Tamaño del proceso \t bloque")
    for x in range(len(proceso)):
        if Order[x] == None:
            print(" \t", proceso[x], "\t\t ", mem_req[x], "\t\t\t no localizado")
        else:
            print(" ", proceso[x], "\t\t", mem_req[x], "\t\t\t", str(Order[x] + 1))
    print()
    return

def Best_fit(n, proceso, mem_req, tam_bloq):
    Order = [None] * n
    flag = [False] * n 
    flag1 = [False] * n
    for i in range(len(mem_req)):
        temp= tam_bloq.copy()
        for j in range(len(mem_req)):
            if min(temp) >= mem_req[i] and flag[i] == False and flag1[tam_bloq.index(min(temp))] == False:
                flag[i] = True
                flag1[tam_bloq.index(min(temp))] = True
                Order[i] = tam_bloq.index(min(temp))
            else:
                temp.remove(min(temp))
    print()
    print("mejor ajuste \n")
    print("proceso  Tamaño del proceso \t bloque")
    for x in range(len(proceso)):
        if Order[x] == None:
            print(" \t", proceso[x], "\t\t ", mem_req[x], "\t\t no localizable")
        else:
            print(" \t", proceso[x], "\t \t", mem_req[x], "\t\t\t", str(Order[x] + 1))
    print()
    return

def worst_fit(n, proceso, mem_req, tam_bloq):
    Order = [None] * n
    flag = [False] * n 
    flag1 = [False] * n
    for i in range(len(mem_req)):
        temp= tam_bloq.copy()
        for j in range(len(mem_req)):
            if max(temp) >= mem_req[i] and flag[i] == False and flag1[tam_bloq.index(max(temp))] == False:
                flag[i] = True
                flag1[tam_bloq.index(max(temp))] = True
                Order[i] = tam_bloq.index(max(temp))
            else:
                temp.remove(max(temp))
    print()
    print("peor ajuste \n")
    print("proceso \t Tamaño del proceso \t bloque")
    for x in range(len(proceso)):
        if Order[x] == None:
            print("\t\t ", proceso[x], "\t ", mem_req[x], "\t\t no localizable")
        else:
            print("\t\t ", proceso[x], " \t\t", mem_req[x], "\t\t", str(Order[x] + 1))
    print()
    return

while (True):
    print("1. Primer ajuste 2. mejor ajuste 3. peor ajuste, 4. salir")
    choice = int(input("elige el algoritmo"))
    
    if choice == 1:
        n = int(input("pon el numero de procesos"))
        proceso = []
        for i in range(1, n + 1):
            proceso.append("j" + str(i))
        mem_req = eval(input("escribe la memoria solicitada"))
        tam_bloq = eval(input("escribe el tamaño del bloque"))
        First_fit(n, proceso, mem_req, tam_bloq)
        
    elif choice == 2:
            n = int(input("pon el numero de procesos"))
            proceso = []
            for i in range(1, n + 1):
                proceso.append("j" + str(i))
            mem_req = eval(input("escribe la memoria solicitada"))
            tam_bloq = eval(input("escribe el tamaño del bloque"))
            Best_fit(n, proceso, mem_req, tam_bloq)
        
    elif choice == 3:
            n = int(input("pon el numero de procesos"))
            proceso = []
            for i in range(1, n + 1):
                proceso.append("j" + str(i))
            mem_req = eval(input("escribe la memoria solicitada"))
            tam_bloq = eval(input("escribe el tamaño del bloque"))
            worst_fit(n, proceso, mem_req, tam_bloq)
    elif choice == 4:
            print("cerrando")
            break
    else:
            print("opcion invalida")
            
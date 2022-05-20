#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:37:28 2021

@author: oliver
"""

#%% Generador de instancias
 
#import os
#os.mkdir(carpeta)
from random import randint
carpeta = "Instances/"
 
# Numero de objetos  (10, 30, 50, 70... 200)
# Valores de objetos, en que rangos  (10-20)
# Pesos de los objetos, en que rangos (10-30)
# Con que capacida     (200, 400, 600)
# Cuantas replicas por cada combinación de parametros (5 replicas)

# Nombrar el archivo en funcion de los parámetros usados en la instancias 
# "ins_n_10_v_51-100_w_10-20_Q_100_rep_1.txt"

list_cap = [200, 400, 600]

for n in range(10,201,20):
    for cap in list_cap:
        for j in range(1, 6):
            nombre = carpeta + "ins_n_" + str(n) + "_v_10-20_w_10-30_Q_" + str(cap) + "_rep_" + str(j)+ ".txt"    
            salida = open(nombre, "a")
            print("n_objs", n, file=salida)
            print("values", file=salida)
            for i in range(n):
                print(randint(10,20), file=salida, end="\t")
            print("\nweights", file=salida)
            for i in range(n):
                print(randint(10,30), file=salida, end="\t")
            print("\ncapacity",  cap, file=salida)
            salida.close()

#%%
len(list(range(10, 201, 20)))

archivo_prueba = open("Instances/nombre3.txt", "a")  # w, r, a, (write, read, append)
archivo_prueba.write("Hola mundo")
archivo_prueba.close()

#%%

n=15
print("n_objs", n)
print("n_objs %d" % n)
print(f"n_objs {n}")
print( "n_objs {}".format(n) )
 
peso= 14.6

prueba= open("prueba.txt", "a")
prueba.write("n_objs %d %f" % (n,peso) )
prueba.close()

#%%
carpeta = "Instances/"
list_cap = [200, 400, 600]

for n in range(10,201,20):
    for cap in list_cap:
        for j in range(1, 6):
            nombre = carpeta + "ins_n_" + str(n) + "_v_10-20_w_10-30_Q_" + str(cap) + "_rep_" + str(j)+ ".txt"    
            salida = open("lista_instancias.txt", "a")
            print(nombre, file=salida)
            salida.close()

          
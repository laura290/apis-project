import os
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

def cargaDataSet():
    global b
    b = pd.read_csv("b.to_csv(apI.csv',index=False,header=True)")
    return b
    
def extraediccionario(listadiccionarios):
    lista=[]
    for diccionario in listadiccionarios:
        for key,value in diccionario.items():
            if key == "ordered_teams":
                lista.append(value)
    return lista


def creaundataframe(listapartidos):
    lista = []
    for a in listapartidos:
        lista.append(pd.DataFrame(a))
    return pd.concat(lista)

def seleccion_pais():
    global b
    data = b[(b["country"]== "France")]
    return b


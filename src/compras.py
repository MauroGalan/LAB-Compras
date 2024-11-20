import csv
from datetime import datetime
from collections import defaultdict
from typing import NamedTuple
Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)])

def lee_compras (ruta:str)->list[Compra]:
    """
    Recibe el nombre de un fichero y devuelve una lista de tuplas de tipo Compra 
    conteniendo todos los datos almacenados en el fichero.
    """
    with open (ruta, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        lista = []
        for dni,super,prov,fecha_l,fecha_s,total in lector:
            fecha_l = datetime.strptime(fecha_l,"%d/%m/%Y %H:%M")
            fecha_s = datetime.strptime(fecha_s,"%d/%m/%Y %H:%M")
            total = float(total)
            lista.append(Compra(dni,super,prov,fecha_l,fecha_s,total))
        return lista
    
def compra_maxima_minima_provincia(compras:list[Compra],provincia:str)->tuple[float,float]:
    """
    Recibe una lista de tuplas de tipo Compra y una provincia. Devuelve una tupla que contiene 
    el importe máximo y el mínimo de las compras que se han realizado en la provincia dada como parámetro. 
    Si la provincia toma el valor None, se devuelve una tupla con el importe máximo y el mínimo calculados a partir 
    de todas las compras.
    """
    importes=[]
    for compra in compras:
        if provincia == None or compra.provincia == provincia:
            importes.append(compra.total_compra)
    return max(importes),min(importes)

def hora_menos_afluencia(compras:list[Compra])->tuple[datetime.hour,int]:
    """
    Recibe una lista de tuplas de tipo Compra y devuelve una tupla con la hora en la que llegan menos clientes 
    y el número de clientes que llegan a dicha hora.
    """
    horas_c = {}
    for compra in compras:
        if compra.fecha_llegada.hour not in horas_c:
            horas_c[compra.fecha_llegada.hour]=0
        horas_c[compra.fecha_llegada.hour]+=1
    return min(horas_c.items(),key= lambda x:x[1])

def supermercados_mas_facturacion(compras:list[Compra],n:int=3)->tuple[int,tuple[str,int]]: 
    """
    Recibe una lista de tuplas de tipo Compra y un número entero n, con valor por defecto 3. 
    Devuelve un ranking, es decir, una lista de tuplas (posición_ranking, (supermercado, facturación)) 
    con las n marcas de supermercados que más facturan, en orden decreciente de facturación. 
    El ranking debe empezar por la posición 1.
    """
    supers=defaultdict(int)
    for compra in compras:
        supers[compra.supermercado]+=compra.total_compra
    supers_ord = sorted(supers.items(), key= lambda x:x[1],reverse=True)
    ranking = []
    for i,tupla in enumerate(supers_ord[:n]):
        ranking.append((i+1,tupla))
    return ranking





    
from compras import *
def test_lee_compras(ruta):
    lista = lee_compras(ruta)
    print(f"Se han leído {len(lista)} registros")
    print(f"Los tres primeros registros son: {lista[:3]}")
    print(f"Los tres últimos registros son: {lista[-3:]}")

def test_compra_max_min(ruta):
    print(f"El importe máximo de Huelva es {compra_maxima_minima_provincia(lee_compras(ruta),"Huelva")[0]} y el mínimo es {compra_maxima_minima_provincia(lee_compras(ruta),"Huelva")[1]}")
    print(f"El importe máximo general es {compra_maxima_minima_provincia(lee_compras(ruta),None)[0]} y el mínimo es {compra_maxima_minima_provincia(lee_compras(ruta),None)[1]}")

def test_hora_men_aflu(ruta):
    hora,personas=hora_menos_afluencia(lee_compras(ruta))
    print(f"La hora con menos afluencia son las {hora} con un número de {personas} clientes")

def test_sup_mas_factu(ruta,n):
    print(f"Los {n} supermercados con mayor facturacion son: {supermercados_mas_facturacion(lee_compras(ruta),n)}")

if __name__ =="__main__":
    #test_lee_compras("data/compras.csv")
    #test_compra_max_min("data/compras.csv")
    #test_hora_men_aflu("data/compras.csv")
    test_sup_mas_factu("data/compras.csv",2)


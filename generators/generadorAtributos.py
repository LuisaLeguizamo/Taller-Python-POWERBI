import random

def generarAtributos():
    tipoProducto=['Musica','TV','APP','PC','Celulares','Tablets','Accesorios']
    datos=[]

    for productos in tipoProducto:
        producto={}
        categoria=random.choice(['Plus','Mega','Basic'])   
        producto=[productos,categoria]
        datos.append(producto)
    return datos
print(generarAtributos())    

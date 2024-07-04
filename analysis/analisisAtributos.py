from generators.generadorAtributos import generarAtributos
import pandas as pd

def analizarAtributos():
    datos=generarAtributos()
    tabla=pd.DataFrame(datos,columns=['productos','categoria'])
    tabla.to_csv('./data/tablaProducto.csv', index=False)
analizarAtributos()
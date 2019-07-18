from main import *
pepe=cliente(1)
pepe.modificarcategoria("general")
pepe.imprimir()
jose=cliente(2)
jose.modificarcategoria("preferencial")
jose.imprimir()
Fp=FilaPreferencial()
Fpn=FilaPreferencial()
Fg=FilaGeneral()
Fp.insertar(jose)
Fg.insertar(pepe)
print("cantidad de prefernecial=",Fp.enfila)
#simulacion de ingreso de clientes
#se piensa clientes pares como generales e impares como preferenciales
maxenfila=0
for i in range(1,100,1):
    pepe=cliente(i)
    if (pepe.dni%2==0):
        pepe.modificarcategoria("general")
        Fg.insertar(pepe)
#se estima un tiempo de atencion de 10 minutos por cliente,
#si pasan mas de 1h la fila se divide en dos       
    if (pepe.dni%2==1):
        pepe.modificarcategoria("preferencial")
        Fp.insertar(pepe)
    maxenfila=maxenfila+1    
    if(maxenfila==6):    
        Fp.abrircajanueva(maxenfila,Fpn)
        Fpn.insertar(pepe)
    maxenfila=0
print("cantidad de general=",Fg.enfila)
print("cantidad de prefernecial=",Fp.enfila)
print("cantidad de prefernecial en la fila nueva=",Fpn.enfila)
#este es un cle 

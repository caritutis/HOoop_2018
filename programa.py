from main import *
pepe=cliente(1)
pepe.modificarcategoria("general")
pepe.imprimir()
jose=cliente(2)
jose.modificarcategoria("preferencial")
jose.imprimir()
Fp=FilaPreferencial()
Fg=FilaGeneral()
Fp.insertar(jose)
Fg.insertar(pepe)
print("cantidad de prefernecial=",Fp.enfila)
#simulacion de ingreso de clientes
#se piensa clientes pares como generales e impares como preferenciales
for i range(1,100,1):
    pepe=cliente(i)
    if (pepe.dni%2=0)
    pepe.modificarcategoria("general")
    else
    pepe.modificarcategoria("preferencial")
#este es un cle 

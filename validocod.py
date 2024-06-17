CC=0
CP=0
CP=int(input("Por favor ingresa el código de pieza de 2 dígitos: "))
print("CP: ,",CP)
CC=int(input("Por favor ingresa el código de componente de 4 dígitos: "))
print("CP: ,",CC)
print ()
#       while CC != 00:
#            tope= 10000
#           if Proc_valido(CC,tope) == True:
aux = CC // 100
print("parte entera:" , aux)
cod_pieza = CC-(aux*100)
print("solo codigo pieza: ",cod_pieza)
print("solo codigo componente: ",CC)
if CP==cod_pieza:
    print("son iguales?", CP, " = ", cod_pieza)
else:
    print("no lo son", CP, " = ", cod_pieza)
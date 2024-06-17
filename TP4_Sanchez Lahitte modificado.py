# Manias - Limpio pantalla
print ("\033[H\033[J")

#****************************************************
# ACA EMPIEZA EL MIO - THE BEST ! :)
#****************************************************
cant_piezas=int(0)
cant_comp=int(0)
CP=int(0) 
CC=int(0)
tope=int(0)
codigo=int(0)
PrC= float(0)
PrT= float()
cod_pieza=int(0)
#***************************************************
# Función que verifica que el código sea válido.
# Devuelve booleano
# HAY QUE SACAR VALIDACIONES MIAS en los textos
#***************************************************
def Proc_valido(codigo,tope):
    if codigo > 0:
        if codigo < tope:
            valido = True
            return True
        else:
            valido = False
            return False
    else:
        valido = False
        return False
#****************************************************
#****************************************************
CP=int(input("Hola, por favor ingresa el código de pieza de 2 digitos, para finalizar ingresar '0': "))
while CP != 00:
    tope = 100
    if Proc_valido(CP,tope) == True:
        cant_piezas=cant_piezas+1
        CC=int(input("Por favor ingresa el código de componente de 4 dígitos: "))
        print ()
        while CC != 00:
            tope= 10000
            if Proc_valido(CC,tope) == True:
                aux = CC // 100
                cod_pieza = CC-(aux*100)
                if CP==cod_pieza:
                    valido = True
                    cant_comp=cant_comp+1
                else:
                    CC=int(input("* ATENCION * El codigo no corresponde a esta pieza, vuelva a ingresarlo: "))
                    valido = False
            if valido == True:
#                    print("El codigo de pieza es: ",CP)
#                    print("El codigo de COMPONENTE es: ",CC)
#                    print("el codigo pieza despues de la validacon con el CP es: ",cod_pieza)
                print("Número de pieza: ",CP," Número de Componente: ",CC)
                PrC=float(input("Ingrese el precio de este componente: "))
                tope=1000
                if Proc_valido(PrC,tope) == True:
                    PrT=PrT+PrC
                    CC=int(input("Ingrese el siguiente componente: "))
                    print()
                else:
                    print(" * * * *  OJO! :) Precio no valido.  Ingrese un precio de componente válido * * * * ")
        print("Finalización de carga de componente para la pieza ",CP)
        print()
        print("La cantidad de componentes cargados de esta pieza procesada ",CP," es: ",cant_comp)
        print("La suma de los componentes cargados de esta pieza es: -----> $ ",PrT)
        print()
    CP=int(input("Seguis cargando otra pieza? Ingresa el CODIGO de PIEZA. Recuerda que el Codigo de Pieza es un nro de 2 digitos y con 0 finalizas: ")) 
    cant_comp=0
    PrT=0      
print("Ud ingresó 0 se termina el programa")
print()
print("La cantidad de piezas procesadas es: ",cant_piezas)
print()
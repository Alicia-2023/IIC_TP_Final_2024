# Manias - Limpio pantalla
print ("\033[H\033[J")
cantcp=0
CP=00
codigo=0
PrecioTotal=0

# **********************************************************************
#  Funcion para validar si el CODIGO está dentro de los valores validos
# **********************************************************************

def validocodigo(codigo):
#    if codigo.isnumeric():
#    if    codigo = int(codigo)
        if codigo<0:
            return False
        elif codigo<=99:
            return True
#        else:
#            return False
        else:
            return False
    
# ***********************************************************************
#  Funcion para validar si el PRECIO está dentro de los valores validos
# ***********************************************************************

def validoprecio(precio):
 # if precio.replace('.','',1).isdigit(): #Funcion que valide si un numero tiene decimales
 #   precio=float(precio)
    if precio<10:
      return False
    elif precio<=999.99:
      return True
    else:
      return False
 # else:
 #   return False

# ********************************    
#  * * * PROGRAMA PRINCIPAL * * *
# ********************************

CP=int(input("Hola, por favor ingresa el código de pieza de 2 digitos, para finalizar ingresar '0': "))
while CP == 00:
    print("Ud ingresó 0 se termina el programa principal")
    print()
    print("Principal La cantidad de piezas procesadas es: ",cantcp)
    print()
validoCP = validocodigo(codigo)
if validocodigo(codigo) == True:
    cantcc = 0
    PrT= 0
    cantcp = cantcp + 1
    print("luego de valido codigo Número de pieza: ",CP)
    
    CC=int(input("luego de valido codigo CP Por favor ingresa el código de componente de por lo menos 2 dígitos o con 0 finaliza la carga de componentes de esta pieza: "))
    print ()
    while CC == 00:
        print("sale porque ingreso 0 Ud ingresó 0, finaliza la carga de componentes de esta pieza")
        print()
        print("El precio total de componentes de esta pieza es: $ ",PrecioTotal)
#        CP=int(input("Ingresa el código de la siguiente pieza de 2 digitos, con '0' finaliza el programa: "))
        print()
    validoCC = validocodigo(codigo)
    if validocodigo(codigo) == True:
        CC=(CC*100)+CP
        print("Su código de componente es: ",CC)
        PrC=float(input("Ingrese el precio de este componente: "))
        validoPrC=validoprecio(PrC)
        if validoPrC == True:
            cantcc = cantcc+1
            PrT = PrT+PrC
            print("El precio ingresado de este componente es: ",PrC)
            print("Ingrese el siguiente codigo de componenete - ***** Solo para ver por donde va *****")
            CC=int(input("Ingrese el siguiente componente: "))
            print()
        else:
            print(" * * * *  OJO! :) Precio no valido.  Ingrese un precio de componente válido * * * * ")
            CC=int(input("Vuelva a ingresar un codigo de componente o 0 para finalizar"))
    else:
        CC=int(input("* ATENCION * El codigo no corresponde a esta pieza, vuelva a ingresarlo: "))
CP=int(input("* ATENCION * El codigo es incorrecto, vuelva a ingresarlo: "))  

      

#****************************************************
#ACA EMPIEZA EL MIO - THE BEST ! :)
#****************************************************
#cant_piezas=int(0)
#cant_comp=int(0)
##CP=int(0) 
#CC=int(0)
#tope=int(0)
#codigo=int(0)
#PrC= float(0)
#PrT= float()
#cod_pieza=int(0)
#***************************************************
# Función que verifica que el código sea válido.
# Devuelve booleano
# HAY QUE SACAR VALIDACIONES MIAS en los textos
#***************************************************
#def Proc_valido(codigo,tope):
#    if codigo > 0:
#        if codigo < tope:
#            valido = True
#            return True
#        else:
#            valido = False
#            return False
#    else:
#        valido = False
#        return False
#****************************************************
#****************************************************
#CP=int(input("Hola, por favor ingresa el código de pieza de 2 digitos, para finalizar ingresar '0': "))
#while CP != 00:
#    tope = 100
#    if Proc_valido(CP,tope) == True:
#        cant_piezas=cant_piezas+1
#        CC=int(input("Por favor ingresa el código de componente de 4 dígitos: "))
#        print ()
#        while CC != 00:
#            tope= 10000
#            if Proc_valido(CC,tope) == True:
#                cod_pieza = CC // 100    
#                if CP==cod_pieza:
#                    valido = True
#                    cant_comp=cant_comp+1
#                else:
#                    CC=int(input("* ATENCION * El codigo no corresponde a esta pieza, vuelva a ingresarlo: "))
#                    valido = False
#            if valido == True:
##                    print("El codigo de pieza es: ",CP)
#                    print("El codigo de COMPONENTE es: ",CC)
#                    print("el codigo pieza despues de la validacon con el CP es: ",cod_pieza)
#                print("Número de pieza: ",CP," Número de Componente: ",CC)
#                PrC=float(input("Ingrese el precio de este componente: "))
#                tope=1000
###                if Proc_valido(PrC,tope) == True:
#                    PrT=PrT+PrC
#                    CC=int(input("Ingrese el siguiente componente: "))
##v                    print()
#                else:
#                    print(" * * * *  OJO! :) Precio no valido.  Ingrese un precio de componente válido * * * * ")
#        print("Finalización de carga de componente para la pieza ",CP)
#        print()
#        print("La cantidad de componentes cargados de esta pieza procesada ",CP," es: ",cant_comp)
#        print("La suma de los componentes cargados de esta pieza es: -----> $ ",PrT)
#        print()
#    CP=int(input("Seguis cargando otra pieza? Ingresa el CODIGO de PIEZA. Recuerda que el Codigo de Pieza es un nro de 2 digitos y con 0 finalizas: ")) 
#    cant_comp=0
#    PrT=0      
#print("Ud ingresó 0 se termina el programa")
#print()
#print("La cantidad de piezas procesadas es: ",cant_piezas)
#print()
# TOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHILE

# CONCEPCION--------------------------------------------
def concepcion() :
    
    entradas_conce = 500
    
    nombre = input('Ingrese su nombre ')
    for n in nombre :
        if n == nombre :
            print('El nombre ya existe intenta con otro')
        else :
            print('Nombre ingresado correctamente')
    
    codigo = input('Ingresa codigo de verificacion mínimo de 6 caracteres, debe tener al menos 1 número y sin espacio en blanco.\n')
    largo = 0
    espacio = ' '
    numero = '123456789'
    
    # valida sobre 6 digitos
    if largo not in codigo <= 6 :
        print('Debe tener al menos 6 digitos')
    else:
        print('VALIDADO')
    
    # valida numero en codigo
    for numero in codigo :
        if numero is not codigo :
            print('Debe tener al menos 1 numero')
        else:
            print('NUMERO VALIDADO')
            
    # valida que no hay espacio        
    for espacio in codigo :
        print('No debe tener espacios')
        if espacio is not codigo :
            print('Debe tener al menos 1 numero')
        else:
            print('SIN ESPAPCIO VALIDADO')
                               
    entradas_conce = entradas_conce -1
    print(f'Stock restante {entradas_conce}')     
                    
# PUENTE ALTO--------------------------------------------       
def puente_alto() :
    
    entradas_PA = 1300
    
    nombre = input('Ingrese su nombre ')
    for n in nombre :
        if n == nombre :
            print('El nombre ya existe intenta con otro')
        else :
            print('Nombre ingresado correctamente')
    
    cantidad_PA = 0
    
    cantidad_PA = input('Ingrese cantidad de entradas 3 MAXIMO ')
    
    if cantidad_PA > 3 :
        print('No debe exceder las 3 entradas')
    else:
        entradas_PA = entradas_PA - cantidad_PA
        print(f'Entrada registrada! Stock restante: {entradas_PA}')
    
# MUELLE VARON--------------------------------------------        
def muelle_varon() :
    
    entradas_MB = 100
    
    nombre = input('Ingrese su nombre ')
    for n in nombre :
        if n == nombre :
            print('El nombre ya existe intenta con otro')
        else :
            entradas_MB = entradas_MB -1
            
    print('Tipo de entrada asignado: G')
    
    print(f'Entrada registrada! Stock restante: {entradas_MB}')
    
    
# MUELLE VERGARA--------------------------------------------
def muelle_vergara() :
    
    entradas_MV = 50
    
    nombre = input('Ingrese su nombre ')
    for n in nombre :
        if n == nombre :
            print('El nombre ya existe intenta con otro')
        else :
            print()
   
#----------------------------------------------------------------------------------
# Mostrar Menu
 
print('TOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHI-LE')
print('1.- Comprar entrada en Concepción.')
print('2.- Comprar entrada en Puente Alto.')
print('3.- Comprar entrada en Muelle Barón, Valparaíso.')
print('4.- Comprar entrada en Muelle Vergara, Viña del Mar.')
print('5.- Salir.')

#----------------------------------------------------------------------------------

# LISTA DE COMPRADORES
nombre = {}

#MAIN

opcion = (input('Seleccione una opción: '))

terminar = False
while not terminar :

    if opcion == '1' :
        concepcion()

    elif opcion == '2' :
        puente_alto()
        
    elif opcion == '3' :
        muelle_varon()

    elif opcion == '4' :
        muelle_vergara()

    elif opcion == '5' :
        print('Programa terminado...')
        terminar = True
        
    else:
        print('Debe ingresar una opción válida!!')
        break

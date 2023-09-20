#Decorador
#Funciones que añaden funcionalidades a otras funciones: 
#Se podría decir que decoran a otras funciones o les añaden funcionalidades

#Estructura: 
#Tres funciones (A, B y C) donde A recibe como parámetro a B para devolver  a C
#El decorador devuelve la función 

#La función A será el decorador y A recibe por parámetro que será la función B, 
#después tenemos la función C que es la función interna y nos devuelve el decorador
#con un return 

#Ejemplo sin decorador

def suma( ):
    print(10 + 10)

def resta( ):
    print(20 - 10)

suma()
resta()

#Ejempo con el decorador


def funcion_decoradora(funcion_parametro): #funcion_decoradora(A), funcion_parametro(B)
    def funcion_interior( ):               #funcion_interior(C)

     #funciones que decoran 
        print("Vamos a realizar un calculo:" )
        funcion_parametro()

     #Acciones acicionales que decoran
        print("Hemos termidado el calculo." )
    return funcion_interior

@funcion_decoradora
def suma( ):
    print(10 + 10)

def resta( ):
    print(20 - 10)

suma()
resta()

#Ejemplo2

# Definir un decorador que verifica si un número es par
def decorador_numero_par(funcion_parametro):
    def funcion_interior(numero):
        if numero % 2 == 0:
            resultado = funcion_parametro(numero)
            return resultado
        else:
            return (numero ,"No es un numero par")
    return funcion_interior

# Aplicar el decorador a una función
@decorador_numero_par
def cuadrado(numero):
    return numero ** 2

# Llamar a la función decorada
numero = 4
resultado = cuadrado(numero)
print(resultado)

numero = 7
resultado = cuadrado(numero)
print(resultado)

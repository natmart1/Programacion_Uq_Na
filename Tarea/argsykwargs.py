class MiClase:
    def __init__(self, *args, **kwargs):
        self.lista = list(args)
        self.diccionario = kwargs

    def __str__(self):
        resultado = "Lista: " + str(self.lista) + "\nDiccionario: " + str(self.diccionario)
        return resultado

    def agregar_elemento(self, elemento):
        self.lista.append(elemento)

    def remover_elemento(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)

    def duplicar_lista(self):
        self.lista *= 2

    def procesar_diccionario(self):
        for clave, valor in self.diccionario.items():
            if isinstance(valor, str):
                self.diccionario[clave] = valor.upper()

    def ciclo_while(self, limite):
        contador = 0
        while contador < limite:
            print("Iteración en ciclo while:", contador)
            contador += 1

    def ciclo_for(self, lista):
        for elemento in lista:
            if isinstance(elemento, int):
                print("Elemento entero en la lista:", elemento)
            elif isinstance(elemento, str):
                print("Elemento cadena en la lista:", elemento)
            else:
                print("Elemento de tipo desconocido en la lista:", elemento)

# Crear una instancia de la clase
objeto = MiClase(1, 2, 3, nombre="Juan", edad=30)

# Imprimir la instancia
print(objeto)

# Agregar un elemento a la lista
objeto.agregar_elemento(4)
print(objeto)

# Remover un elemento de la lista
objeto.remover_elemento(2)
print(objeto)

# Duplicar la lista
objeto.duplicar_lista()
print(objeto)

# Procesar el diccionario
objeto.procesar_diccionario()
print(objeto)

# Ejecutar un ciclo while
objeto.ciclo_while(3)

# Ejecutar un ciclo for
mi_lista = [1, "dos", 3.0, "cuatro"]
objeto.ciclo_for(mi_lista)

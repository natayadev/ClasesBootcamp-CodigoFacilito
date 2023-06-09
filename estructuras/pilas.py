class Pila:
    def __init__(self):
        self.lista = []

    def lista_vacia(self):
        return len(self.lista) == 0
    
    def obtener_top(self):
        if self.lista_vacia():
            return None
        return self.lista[-1]
    
    def agregar_elemento(self,elemento):
        self.lista.append(elemento)

    def quitar_elemento(self):
        lista_nueva = self.lista.pop()
        return lista_nueva

if __name__ == "__main__":
    pila = Pila()
    print(pila.lista_vacia())
    pila.agregar_elemento("Libro1")
    pila.agregar_elemento("Libro2")
    pila.agregar_elemento("Libro3")
    pila.agregar_elemento("Libro4")
    print(pila.lista)
    print(pila.obtener_top())
    print(pila.quitar_elemento())
    print(pila.lista)
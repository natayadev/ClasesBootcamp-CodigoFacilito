class Cola:
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
        lista_nueva = self.lista.pop(0)
        return lista_nueva

if __name__ == "__main__":
    cola = Cola()
    print(cola.lista_vacia())
    cola.agregar_elemento("Nata")
    cola.agregar_elemento("Edu")
    cola.agregar_elemento("Jani")
    cola.agregar_elemento("Uriel")
    print(cola.lista)
    cola.quitar_elemento()
    print(cola.lista)

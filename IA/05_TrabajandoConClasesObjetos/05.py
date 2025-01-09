class Restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.menu = []

    def añadirPlato(self, plato):
        self.menu.append(plato)
        print(f"Se ha añadido el plato '{plato}' al menú.")

    def mostrarMenu(self):
        if self.menu:
            print(f"Menú de {self.nombre} ({self.tipo_cocina}):")
            for idx, plato in enumerate(self.menu, 1):
                print(f"{idx}. {plato}")
        else:
            print(f"El menú de {self.nombre} está vacío.")

    def tomarPedido(self, numero_pedido):
        if 1 <= numero_pedido <= len(self.menu):
            plato_elegido = self.menu[numero_pedido - 1]
            print(f"Se ha tomado el pedido: {plato_elegido}")
        else:
            print("Número de pedido inválido. Por favor, elige un plato del menú.")

restaurante = Restaurante("El Sabor Mexicano", "Mexicana")

restaurante.añadirPlato("Tacos al pastor")
restaurante.añadirPlato("Enchiladas verdes")
restaurante.añadirPlato("Guacamole con totopos")

restaurante.mostrarMenu()

restaurante.tomarPedido(2)  

restaurante.tomarPedido(5)  

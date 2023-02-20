#Abstracción 
class Cazador:
    def __init__(self, nombre, espada):
        self.nombre = nombre
        self.espada = espada
    #Métodos
    def presentar(self):
        print(f'Mi nombre es {self.nombre} y mi espada es {self.espada}')
    def ataque(self):
        print("Ataque")
    def defensa(self):
        print("Defendiendo")

class Pilar(Cazador):
    def __init__(self,nombre, espada, respiracion, posturas):
        super().__init__(nombre, espada)
        self.respiracion = respiracion
        self.posturas = posturas

    def presentarPilar(self):
        print(f'Mi nombre es {self.nombre} y mi espada es {self.espada} mi respiración Respiración de {self.respiracion} y tengo {self.posturas}')
    
cazador1 = Cazador("Tanjiro", "Espada Negra")
cazador1.presentar()
print('---------------------------------------------------')
rengoku = Pilar("Rengoku", "Color Roja", "Llama", 9) #Instanciar
rengoku.presentarPilar()
rengoku.presentar()
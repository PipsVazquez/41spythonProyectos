class Carro:
    #Atributos
    #Marca, moldelo, anio, color, numeroSerie, cilindro, tipoMotor
    def __init__(self, marca, modelo, anio, color, numeroSerie, cilindro, tipoMotor):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.__numeroSerie = numeroSerie
        self.cilindro = cilindro
        self.tipoMotor = tipoMotor

    #metodos
    def avanzar(self):
        print("Avanzando")
    
    def frenar(self):
        print("Frenando")
    
    def verificarTenencia(self):
        if self.anio < 2010:
            return True
        else:
            return False

    def calcularTenencia(self):
        if camry.verificarTenencia == False:
            return 1000*1.15
        else: 
            return "No pagas tenencia"

    def presentar(self):
        print(f'{self.marca}\n{self.modelo}\n{self.anio}\n{self.color}\n{self.__numeroSerie}\n{self.cilindro}\n{self.tipoMotor}')
    
    def getNumeroSerie(self):
        print(self.__numeroSerie)

camry = Carro("Toyota", "camry", 2009, "blanco", "x0001", 6, "hibrido") #Instanciar
camry.presentar()
#camry.numeroSerie = "x0001" #Se creó otro atributo y se le asigno un valor pero sigue teniendo el atributo encapsulado.
#print(camry.getnumeroSerie)
camry.getNumeroSerie()
print(camry.verificarTenencia())
print(camry.calcularTenencia())

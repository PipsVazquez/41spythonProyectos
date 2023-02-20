#Abstracción 
class Pilares:
    #Propiedades/Atributos
    #Constructor -> Es el bloque para asignar las propiedades del objeto
    #Init permite inicilizar los valores del constructor
    def __init__(self, nombre, espada, respiracion, posturas, nivelPoder):
        self.nombre = nombre
        self.espada = espada
        self.respiracion = respiracion
        self.posturas = posturas
        self.nivelPoder = nivelPoder
        self.tipo = "humano"
    #Métodos
    def ataque(self):
        print("Ataque")
    def defensa(self):
        print("Defendiendo")

class Aprendiz(Pilares):
    pass

#Pilares
himejima = Pilares("Himejima", "Bolas picos", "Respiración de la Roca", 5, 100)
rengoku = Pilares("Rengoku", "Katana rojo carmesí", "Respiración de llama", 9, 70)

#Lunas
lunaSuperior1 = Pilares("Kokushibo", "Katana Lunar", "Respiración Lunar", 9, 120)
lunaSuperior1.tipo= "Demonio"


#APrendiz1
aprendiz1 = Aprendiz()







print(f'El personaje {aprendiz1.nombre}, su arma es {aprendiz1.espada} su respiracion es {aprendiz1.respiracion}, tiene {aprendiz1.posturas} posturas y tiene {aprendiz1.nivelPoder} de nivel de poder')

print("------------------")



print(f'El personaje {himejima.nombre}, su arma es {himejima.espada} su respiracion es {himejima.respiracion}, tiene {himejima.posturas} posturas y tiene {himejima.nivelPoder} de nivel de poder')

print("------------------")

print(f'El personaje {rengoku.nombre}, su arma es {rengoku.espada} su respiracion es {rengoku.respiracion}, tiene {rengoku.posturas} posturas y tiene {rengoku.nivelPoder} de nivel de poder')


print("------------------")

print(f'El personaje {lunaSuperior1.nombre}, su arma es {lunaSuperior1.espada} su respiracion es {lunaSuperior1.respiracion}, tiene {lunaSuperior1.posturas} posturas y tiene {lunaSuperior1.nivelPoder} de nivel de poder y es {lunaSuperior1.tipo}')
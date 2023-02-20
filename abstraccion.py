#Abstracción 
class Pilares:
    #Propiedades/Atributos
    nombre = " "
    edad = 18
    espada = "normal"
    estatura = 1.6
    respiracion = "normal"
    postura = " "
    #Métodos
    def ataque(self):
        print("Ataque")
    
    def defensa(self):
        print("Defendiendo")

#SE crea el objeto a partir de la clase
personajeMizunoto = Pilares()
personajeMizunoto.nombre = "Pips"

personajeTsuguko = Pilares()
personajeTsuguko.nombre = "Kanao"

print(f'El personaje {personajeMizunoto.nombre}, tiene {personajeMizunoto.edad} años y su respiración es {personajeMizunoto.respiracion}')

print(f'El personaje {personajeTsuguko.nombre}, tiene {personajeTsuguko.edad} años y su respiración es {personajeTsuguko.respiracion}')

kibutzuji = input("Está cerca el enemigo? ")



if kibutzuji == "si":
    personajeMizunoto.ataque()
else: 
    personajeMizunoto.defensa()
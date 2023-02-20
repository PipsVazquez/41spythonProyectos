import turtle
turtle.shape("turtle")

continuar = input(" Bienvenido al graficador. Presiona si para graficar y no para terminar")
contador = 0
while contador <= 5:
    #grados = int(input("Ingresa los grados de la figura"))
    print('''     Selecciona la opcion a graficar
        1) Triángulo
        2) Cuadrado
        3) Pentágono ''')
    opcion = int(input())

    if opcion == 1:
        grados = 360/3
        turtle.forward(100)
        turtle.left(grados)
        turtle.forward(100)
        turtle.left(grados)
        turtle.forward(100)
        turtle.left(grados)

    elif opcion == 2:
        grados = 360/4
        turtle.forward(100)
        turtle.left(grados)
        turtle.forward(100)
        turtle.left(grados)
        turtle.forward(100)
        turtle.left(grados)
        turtle.forward(100)
        turtle.left(grados)

    elif opcion == 3:
        grados = 360/5
        turtle.forward(100)
        turtle.left(grados)
        turtle.forward(100)
        turtle.left(grados)
        turtle.forward(100)
        turtle.left(grados)
        turtle.forward(100)
        turtle.left(grados)
        turtle.forward(100)
        turtle.left(grados)

    else: 
        print("Comando invalido")
        print('''
            ______
            .-"      "-.
        /            \
        |              |
        |,  .-.  .-.  ,|
        | )(__/  \__)( |
        |/     /\     \|
        (_     ^^     _)
        \__|IIIIII|__/
            | \IIIIII/ |
            \          /
    jgs    `--------`
    
    ''')

    #continuar = input(" Bienvenido al graficador. Presiona si para graficar y no para terminar")
    contador += 1
print("programa terminado")
turtle.exitonclick()
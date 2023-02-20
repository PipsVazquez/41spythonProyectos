import turtle
turtle.shape('turtle')

lados = int(input("Escribe el número de lados de la figura que quieres: "))
longitud = int(input("Escribe la longitud de cada lado: "))
numeroFiguras = int(input())

for j in range(0, numeroFiguras):
#    turtle.fillcolor("orange")
#    turtle.begin_fill()
    for i in range(0, lados):
        turtle.forward(longitud)
        turtle.right(360/lados)
#    turtle.end_fill()
    turtle.right(360/numeroFiguras)
turtle.exitonclick()
import turtle

ventana = turtle.Screen()
ventana = turtle.bgcolor('black')
tortuga = turtle.Turtle()
tortuga.speed(50)
tortuga.color('red')

numero_estrella = 75

for i in range(numero_estrella * 5):
    tortuga.forward(i*3)
    tortuga.right(145)

ventana.exitonclik()








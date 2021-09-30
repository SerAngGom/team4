#importar tortuga
from turtle import *

#Dimensiones de la pantalla
pantalla = Screen()
pantalla.setup (500, 500)
pantalla.screensize (550, 550)

# Variables de movimiento de la tortuga

x = int(input(' Elige la coordena x de la posición inicial de la tortuga: '))
y = int(input(' Elige la coordena y de la posición inicial de la tortuga: '))

radio = int(input(' Indica el radio del arco que quieres dibujar: '))

angulo = int(input(' Indica el angulo que quieres dibujar: '))

# Movimientos de la tortuga
tortuga = Turtle()
tortuga.penup()
tortuga.goto(x,y)
tortuga.pendown()
tortuga.forward(radio)
tortuga.left(90)
tortuga.circle(radio,angulo)
tortuga.goto(x,y)
tortuga.penup()
tortuga.goto(x, y-1)
tortuga.hideturtle()


#printeo los datos de entrada
tortuga.write('({0},{1}) radio = {2} angulo = {3}'.format(x,y,radio,angulo))

pantalla.exitonclick()




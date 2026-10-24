import turtle


print("Welcome to my artwork")
screen = turtle.Screen 
turtle.Screen().bgcolor("black")
turtle.Screen().title("My project artwork")

pen = turtle.Turtle
turtle.speed(150)
turtle.hideturtle()

def draw_petal(size,colour): any

turtle.begin_fill()
turtle.circle(2)
turtle.end_fill()
colours = ["red","orange","yellow","lime","cyan","violet","pink","white"]

for i in range(36):
    turtle.color(colours[i%len(colours)])
    turtle.width(2)
    turtle.forward(i*2)
    turtle.right(10)

turtle.up()
turtle.goto()
turtle.down()

turtle.done
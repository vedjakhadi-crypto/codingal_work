import turtle


print("This is a demo on how to create a neon mandela effect")


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Our first turtle project(NM)")


pen = turtle.Turtle()
pen.speed("fastest")
pen.hideturtle()

colours = ["red","orange","yellow","lime","cyan","violet","pink","white"]
for i in range(80):
    pen.color(colours[i%len(colours)])
    pen.width(2)
    pen.forward(i*2)
    pen.right(91)
turtle.done()



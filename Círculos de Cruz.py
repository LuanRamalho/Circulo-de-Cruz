from turtle import *
title("Circulos de Cruz")

screensize(150, 150)
colormode(255)
hideturtle()

penup()
goto(0, 80)
dot(40, 0, 250, 55)
goto(0, 40)
dot(40, 255, 100, 70)
goto(0, 0)
dot(40, 200, 150, 200)
goto(0, -40)
dot(40, 0, 255, 0)
goto(0, -80)
dot(40, 255, 150, 50)
goto(40,0)
dot(40, 50, 255, 255)
goto(80,0)
dot(40, 50, 150, 50)
goto(-40,-0)
dot(40, 255, 255, 50)
goto(-80,-0)
dot(40, 0, 50, 250)
mainloop()
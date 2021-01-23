import turtle,random

space=[-70,-40,-10,20,50,80]
color=["red","green","yellow","blue","orange","skyblue"]
screen=turtle.Screen()
screen.setup(width=500,height=400)

bet=turtle.textinput(title="enter bet",prompt="enter the your color of your turtle you want to  bet")
turt=[]
for i in range(6):
   jerry=turtle.Turtle(shape="turtle")
   jerry.color(color[i])
   jerry.penup()
   jerry.goto(-300,0+space[i])
   turt.append(jerry)
x=True
while x:
   for i in turt:
      if i.xcor() > 230:
         wc=i.pencolor()
         if wc== bet:
            print("you  win")
         else:
            print("lost")
         x=False
      num=random.randint(1,10)
      i.forward(num)

screen.exitonclick()


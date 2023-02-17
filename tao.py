import turtle

tao = turtle.Pen()
tao.shape('turtle')

for i in range(4):
    tao.forward(100)
    tao.left(90)
tao.penup()

tao.goto(x=80,y=80)
tao.pendown()
for i in range(4):
    tao.forward(100)
    tao.left(90)
tao.penup()

tao.goto(x=-80,y=-80)
tao.pendown()
for i in range(4):
    tao.forward(100)
    tao.left(90)
tao.penup()

tao.goto(x=80,y=-80)
tao.pendown()
for i in range(4):
    tao.forward(100)
    tao.left(90)
tao.penup()

tao.goto(x=-80,y=80)
tao.down()
for i in range(4):
    tao.forward(100)
    tao.left(90)
tao.penup()

tao.goto(x=160,y=160)
tao.pendown()
for i in range(8):
    tao.forward(25)
    tao.left(45)
tao.penup()

tao.goto(x=-80,y=-120)
tao.pendown()
for i in range(8):
    tao.forward(25)
    tao.left(45)
tao.penup()

tao.goto(x=160,y=-120)
tao.pendown()
for i in range(8):
    tao.forward(25)
    tao.left(45)
tao.penup()

tao.goto(x=-80,y=160)
tao.pendown()
for i in range(8):
    tao.forward(25)
    tao.left(45)
tao.penup()

tao.goto(x=-180,y=-180)
tao.pendown()
for i in range(4):
    tao.forward(460)
    tao.left(90)
tao.penup()

tao.goto(x=-140,y=-140)
tao.pendown()
for i in range(4):
    tao.forward(380)
    tao.left(90)
tao.penup()

tao.right(135)
tao.pendown()
tao.forward(58)
tao.penup()

tao.goto(x=-140,y=240)
tao.right(90)
tao.pendown()
tao.forward(58)
tao.penup()

tao.goto(x=240,y=240)
tao.right(90)
tao.pendown()
tao.forward(58)
tao.penup()

tao.goto(x=240,y=-140)
tao.right(90)
tao.pendown()
tao.forward(58)
tao.penup()

tao.goto(x=-260,y=260)
    

import turtle

#This code creates dressage arena size 20m x 60m
t=turtle.Turtle()
turtle.setworldcoordinates(-400,-100,700,700)
a=200
b=600
print(t.pos())
t.write('A')
t.left(90)
t.penup()
t.forward(15)
t.right(90)
t.pendown()
t.forward(a/2)
t.left(90)
t.forward(b/10)
print(t.pos())
t.write('F', align='left')
t.forward(b/5)
print(t.pos())
t.write('P', align='left')
t.forward(b/5)
print(t.pos())
t.write('B', align='left')
t.forward(b/5)
print(t.pos())
t.write('R', align='left')
t.forward(b/5)
print(t.pos())
t.write('M', align='left')
t.forward(b/10)
t.left(90)
t.forward(a/2)
print(t.pos())
t.write('C',  align='center')
t.forward(a/2)
t.left(90)
t.forward(b/10)
print(t.pos())
t.write('H', align='right')
t.forward(b/5)
print(t.pos())
t.write('S', align='right')
t.forward(b/5)
print(t.pos())
t.write('E', align='right')
t.forward(b/5)
print(t.pos())
t.write('V', align='right')
t.forward(b/5)
print(t.pos())
t.write('K', align='right')
t.forward(b/10)
t.left(90)
t.forward(a/2)
print(t.pos())
turtle.mainloop()
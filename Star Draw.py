col = ('yellow','red', 'green','orange','blue','white')

t.speed(30)

for i in range (350):
    t.color(col[i%5])
    t.forward(1*4)
    t.left(150)
    t.width(2)
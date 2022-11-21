import turtle # behívja a "turtle" könyvtárat

ablak = turtle.Screen() # létre hoz egy kijelzési alapot
teki = turtle.Turtle() # létre hoz egy "teknős" ecsetet

teki.right(90) # jobbra fordul 90 fokkal
teki.left(3600) # balra megfordul 10x
teki.right(-90) # balra fordul 90 fokkal
teki.speed(10) # 10-esre változik a gyorsasága
teki.left(3600) # balra megfordul 10x csak most gyorsabban
teki.speed(0) # a gyorsasága 0 lesz
teki.left(3645) # 10x megfordul balra + 45 fokkal balra menne 
teki.forward(-100) # hátra megy 10 pixelt 
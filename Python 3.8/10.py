import turtle # behívja a "turtle" könyvtárat

ablak = turtle.Screen() # létre hoz egy kijelzési alapot
teki = turtle.Turtle() # létre hoz egy "teknős" ecsetet

teki.right(90) # jobbra fordul 90 fokkal
teki.left(3600) # balra megfordul 10x
teki.right(-90) # balra fordul 90 fokkal
teki.speed(10) # 10-esre változik a sebessége
teki.left(3600) # balra megfordul 10x csak most gyorsabban
teki.speed(0) # megáll
teki.left(3645) # 10x megfordulna balra + 45 fokkal balra menne 
teki.forward(-100) # hátra menne 10 pixelt 
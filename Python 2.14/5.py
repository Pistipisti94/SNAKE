a = 10000   # alaptőke
b = 0.08    # névleges kamatláb
c = 12     # évközi kamatozások száma
d = int(input("Írd be hány évre szeretnéd a kamatozást: ")) # futamidő

xy = (a * ((1 + b / c) ** (c * d)))

print("A betét értéke:", xy)
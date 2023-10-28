koord = input("введите координаты клетки\n")
bukv = koord[0]
chi = int(koord[1])
if chi % 2 == 0 and bukv == "a" or bukv == "c" or bukv == "e" or bukv == "g":
    print("клетка белая")
else:
    print("клетка чёрная")
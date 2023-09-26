a = int(input("Digite o valor de A"))
b = int(input("Digite o valor de B"))
c = int(input("Digite o valor de C"))
if a >= b and a >= c:
    if b >= c:
        print("a ordem é:", a, b, c)
    else:
        print("a ordem é:", a, c, b)
elif b >= a and b >= c:
    if a >= c:
        print("a ordem é:", b, a, c)
    else:
        print("a ordem é:", b, c, a)
else:
    if a >= b:
        print("a ordem é:", c, a, b)
    else:
        print("a ordem é:", c, b, a)
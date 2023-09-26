n1 = float(input("Digite a primeira nota"))
n2 = float(input("Digite a segunda nota"))
n3 = float(input("Digite a terceira nota"))
ME = 0
MA = (n1 + n2 * 2 + n3 * 3 + ME) / 7
if MA >= 90:
    print("Sua nota foi A")
elif MA >= 75 and MA < 90:
    print("Sua nota foi B")
elif MA >= 60 and MA < 75:
    print("Sua nota foi C")
elif MA >= 40 and MA < 60:
    print("Sua nota foi C")
else:
    print("Sua nota foi E")
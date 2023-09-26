H = float(input("Digite a sua altura"))
P = float(input("Digite seu peso"))
IMC = P / (H * H)
print(round(IMC , 1))
if IMC < 18.5:
    print("Abaixo do peso")
if IMC > 18.5 and IMC < 25:
    print("Peso normal")
if IMC > 25 and IMC < 30:
    print("Acima do peso")
if IMC > 30:
    print("Obeso")


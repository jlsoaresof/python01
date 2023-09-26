Valor = 1200.0
FP = input("digite a forma de pagamento")
dez = Valor * 0.1
quinze = Valor * 0.15
if FP == "Dinheiro" or "Cheque":
    print(Valor - dez)
if FP == "Cartão a vista":
    print(Valor - quinze)
if FP == "Etiqueta":
    print(Valor * 0.1)
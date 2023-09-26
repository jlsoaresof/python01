bruto = float(input("Digite o quanto você ganha: "))
sete = bruto * 0.075
quinze = bruto * 0.15
doisdois = bruto * 0.225
doissete = bruto * 0.275
if bruto >= 1903.99 and bruto <= 2826.65:
    print("seu salário líquido é de:" , bruto - sete)
    print("você está dando pro governo:" , sete)
if bruto < 1903.99:
    print("Seu salário é de:" , round(bruto , 1))
elif bruto >= 2826.66 and bruto <= 3751.05:
    print("seu salário líquido é de:" , round(bruto - quinze , 1))
    print("você está dando pro governo:" , round(quinze , 1))
elif bruto >= 3751.06 and bruto <= 4664.68:
    print("seu salário líquido é de:" , round(bruto - doisdois , 1))
    print("você está dando pro governo:" , round(doisdois , 1))
elif bruto >= 4664.68:
    print("seu salário líquido é de:" , round(bruto - doissete , 1))
    print("você está dando pro governo:" , round(doissete , 1))

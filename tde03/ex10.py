dolar = 5.07
euro = 5,45
libra = 6.37

moeda = int(input(f"Qual moeda vc quer(1 - dolar; 2 - Euro; 3 - libra)"))
valor = float(input(f'Quantos {moeda}??'))

if moeda == 1:
    din = valor * dolar 
elif moeda == 2:
    din = valor * euro 
else:
    din = valor * libra 

if din >= 1000:
    print(f"O valor do cambio ficou {din} e sera cobrado uma comição de 5% então o valor final sera {din * 1.05}")
else:
    print(f"O valor do cambio ficou {din} e sera cobrado uma comição de 3% então o valor final sera {din * 1.03}")
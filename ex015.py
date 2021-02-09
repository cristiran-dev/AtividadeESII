#Tabela de preço de aluguel de carro
km = int(input('Quantos Kilometros o carro percorreu? '))
d = float(input('Quantos dias o carro foi alugado? '))
p = (km * 0.15) + (d * 60)
print('O preço a pagar pelo aluguel do carro e R${:.2f}'.format(p))

salário = float(input('Qual o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganahava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salário, novo))

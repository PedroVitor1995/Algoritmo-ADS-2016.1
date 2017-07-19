"""45. Um algoritmo para gerenciar os saques de um caixa eletronico deve possuir algum mecanismo para
decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que realizou o
saque. Um possivel criterio seria o da "distribuicao otima" no sentido de que as notas de menor valor
disponiveis fossem distribuidas em numero minimo possivel. Por exemplo, se a maquina so dispoe de
notas de 50, de 10, de 5 e de 1, para uma quantia solicitada de 87, o algoritmo deveria
indicar uma nota de 50, tres notas de 10, uma nota de 5 e duas notas de 1. Escreva um
algoritmo que receba o valor da quantia solicitada e retorne a distribuicao das notas de acordo com o
criterio da distribuicao otima."""

quantia = input ('Digite o valor da quantia solicitada: ')

nota100 = quantia / 100
nota50 = quantia % 100 / 50
nota20 = quantia % 100 % 50 / 20
nota10 = quantia % 100 % 50 % 20 / 10
nota5 = quantia % 100 % 50 % 20 % 10 / 5
nota1 = quantia % 100 % 50 % 20 % 10 % 5

print ('\nO numero de notas de cada valor que deve ser disponibilizado para o cliente e  ')
print ('\n %d nota de 100 reais %d nota de 50 reais %d nota de 20 reais %d nota de 10 reais %d nota de 5 reais e %d nota 1 real') % (nota100,nota50,nota20,nota10,nota5,nota1)

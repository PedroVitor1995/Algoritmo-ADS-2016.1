"""35. Leia um numero inteiro (4 digitos), calcule e escreva a soma dos elementos que o compoem. Ex.:
numero = 9534 ; soma = 9+5+3+4 = 21."""

numero = input ('Digite um numero inteiro de 4 digitos: ')

n1 = numero / 1000
n2 = (numero % 1000) / 100
n3 = (numero % 1000) % 100 / 10
n4 = (numero % 1000) % 100 % 10

soma = n1 + n2 + n3 + n4

print ('\nA soma dos elementos e %d') %(soma)
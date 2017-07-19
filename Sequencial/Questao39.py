"""39. Leia tres numeros inteiros e positivos (A, B, C) e calcule a seguinte expressao:"""

A = input ('Digite o primeiro numero inteiro: ')
B = input ('\nDigite o segundo numero inteiro: ')
C = input ('\nDigite o terceiro numero inteiro: ')

R = (A + B) ** 2
S = (B + C) ** 2

D = (R + S) / 2

print ('\nO valor da expressao e %d') % (D)
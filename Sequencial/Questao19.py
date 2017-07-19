"""19. Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)"""

r = input ('Digite o valor do raio de uma esfera: ')

p = 3.14
v = 4 * p * (r ** 3) / 3

print ('\nO volume da esfera e %.2f ') % (v)

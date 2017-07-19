"""43. Um sistema de equacoes lineares do tipo , pode ser resolvido segundo mostrado abaixo
Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, calcule e escreva os valores de x e y."""

a = input ('Digite o valor de a: ')
b = input ('\nDigite o valor de b: ')
c = input ('\nDigite o valor de c: ')
d = input ('\nDigite o valor de d: ')
e = input ('\nDigite o valor de e: ')
f = input ('\nDigite o valor de f: ')

x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

print ('\nO valor de x e %.2f ') % (x)
print ('\nO valor de y e %.2f ') % (y)
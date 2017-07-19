"""12. Leia o salario de um trabalhador e escreva seu novo salario com um aumento de 25%."""

salario = input ('Digite o seu salario: ')

novo_salario = (salario * 0.25) + salario

print ('\nSeu novo salario com aumento de 25%% e %.2f') % (novo_salario)
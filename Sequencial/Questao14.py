"""14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a media ponderada."""

nota1 = input ('Digite a primeira nota: ')
nota2 = input ('\nDigite a segunda nota: ')
nota3 = input ('\nDigite a terceira nota: ')
peso1 = input ('\nDigite o peso da primeira nota: ')
peso2 = input ('\nDigite o peso da segunda nota: ')
peso3 = input ('\nDigite o peso da terceira nota: ')

soma_nota = nota1 * peso1 + nota2 * peso2 + nota3 * peso3
soma_peso = peso1 + peso2 + peso3

media_ponderada = soma_nota / soma_peso 

print ('\nA media poderada e %.2f') % (media_ponderada)
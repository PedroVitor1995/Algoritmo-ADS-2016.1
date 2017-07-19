# -*- coding: utf-8 -*-
"""14. Leia 3 notas de um aluno e o peso de cada nota,
calcule e escreva a média ponderada."""
nota_um = input("Escreva a nota um: ")
nota_dois = input("Escreva a nota dois: ")
nota_tres = input("Escreva a nota três: ")
peso_um = input("Escreva o peso da nota um: ")
peso_dois = input("Escreva o peso da nota dois: ")
peso_tres = input("Escreva o peso da nota três: ")
termos_de_cima = nota_um * peso_um + nota_dois * peso_dois + nota_tres * peso_tres
termos_de_baixo = peso_um + peso_dois + peso_tres
cauculando_a_media = termos_de_cima / termos_de_baixo
print "A média ponderada de %d , %d, %d, considerando os pesos %d , %d , %d respectivamente é: %d " % (nota_um,nota_dois,nota_tres,peso_um,peso_dois,peso_tres,cauculando_a_media)


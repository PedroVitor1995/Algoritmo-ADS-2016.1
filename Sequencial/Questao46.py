"""46. Uma loja vende seus produtos no sistema entrada mais duas prestacoes, sendo a entrada maior ou igual a
cada uma das duas prestacoes; estas devem ser iguais, inteiras e as maiores possiveis. Por exemplo, se o
valor da mercadoria for 270,00, a entrada e as duas prestacoes sao iguais a 90,00; se o valor da
mercadoria for 302,00, a entrada e de 102,00 e as duas prestacoes sao iguais a 100,00.
Escreva um algoritmo que receba o valor da mercadoria e forneca o valor da entrada e das duas
prestacoes, de acordo com as regras acima."""


valor_mercadoria = input ('Digite o valor da mercadoria:')

valor_entrada = (valor_mercadoria / 3) + (valor_mercadoria % 3)
valor_prestacao = valor_mercadoria / 3

print ('\nO valor da entrada e %d reais ') % (valor_entrada)
print ('\nO valor das duas prstacoes e %d reais ') % (valor_prestacao)
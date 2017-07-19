"""41. O custo ao consumidor de um carro novo e a soma do custo de fabrica com a percentagem do
distribuidor e dos impostos (aplicados ao custo de fabrica). Supondo que a percentagem do distribuidor
seja de 28%  e os impostos de 45%, escreva um algoritmo que leia o custo de fabrica de um carro e
escreva o custo ao consumidor."""

custo_fabrica = input ('Digite o custo de fabrica de um carro: ')

distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45

custo_consumidor = custo_fabrica + distribuidor + impostos

print ('O custo ao consumidor com a percentagem  distribuidor e dos impostos e %.2f') % (custo_consumidor)
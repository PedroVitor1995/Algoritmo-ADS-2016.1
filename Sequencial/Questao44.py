"""44. Sabendo que latao e constituido de 70%  de cobre e 30%  de zinco, escreva um algoritmo que calcule a
quantidade de cada um desses componentes para se obter certa quantidade de latao (em kg), informada
pelo usuario."""

quantidade_latao = input ('Digite a quantidade de latao (em kg): ')

latao1 = quantidade_latao * 1000
cobre = latao1 * 0.70
zinco = latao1 * 0.30

print ('A quantidade de cobre e zinco em %d kg de latao e %2.f gramas de cobre e %2.f gramas de zinco ') % (quantidade_latao,cobre,zinco)
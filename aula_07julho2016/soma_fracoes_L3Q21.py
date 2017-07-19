"""
    Somar Fracoes S = 1/1 + 3/2 + 5/3 + 7/4... + 99/50
    Pythonic Way: sum([Fraction(i+i-1, i) for i in range(1, input('N: ')+1)])
"""
from soma_fracoes_L3Q17 import calcular_mmc_sequencia


def main():
    numero = input("Quantas Fracoes? ")
    soma_fracoes(numero)


def soma_fracoes(numero):
    mmc = calcular_mmc_sequencia(numero)
    print 'MMC = %d' % mmc
    numerador_final = 0
    for i in range(1, numero + 1):
        denominador = i
        numerador = i + i - 1
        print '%d/%d + ' % (numerador, denominador),
        numerador_final = numerador_final + ((mmc / denominador) * numerador)

    print 'Resultado = %d/%d == %.2f' % (numerador_final, mmc, (numerador_final/float(mmc)))


if __name__ == '__main__':
    main()
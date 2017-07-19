"""
    Somar Fracoes S = 1/1 - 1/2 + 1/3 - 1/4... +/- 1/N
    sum([Fraction(1, i) if i % 2 == 1 else Fraction(1,-i) for i in range(1, 5)])
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
        if denominador % 2 == 0:
            denominador = denominador * -1

        print '%d/%d + ' % (1, denominador),
        numerador_final = numerador_final + ((mmc / denominador) * 1)

    print 'Resultado = %d/%d == %.2f' % (numerador_final, mmc, (numerador_final/float(mmc)))


if __name__ == '__main__':
    main()
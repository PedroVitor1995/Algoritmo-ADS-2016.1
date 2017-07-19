# By E.
def main():
    num1, num2 = input('N1: '), input('N2: ')
    resultado = mmc(num1, num2)
    print 'MMC = %d' % resultado


def mmc(numero1, numero2):
    multiplo = 1

    while multiplo % numero1 != 0 or multiplo % numero2 != 0:
        multiplo = multiplo + 1

    return multiplo


if __name__ == '__main__':
    main()

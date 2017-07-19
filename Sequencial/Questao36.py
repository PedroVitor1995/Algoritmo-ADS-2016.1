"""36. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias."""

anos = input ('Digite a idade de uma pessoa em anos: ')
meses = input ('Digite a idade de uma pessoa em meses: ')
dias = input ('Digite a idade de uma pessoa em dias: ')

dias1 = anos * 365
dias2 = meses * 30

total_dias = dias1 + dias2 + dias

print ('\nA idade dessa pessoa de %d anos %d meses %d dias expressa em dias e %d dias ') % (anos,meses,dias,total_dias)
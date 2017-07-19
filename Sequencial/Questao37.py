"""37. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias."""

dias = input ('Digite a idade de uma pessoa em dias: ')

anos = dias / 365
meses = (dias % 365) /30
dias1 = (dias % 365) % 30

print ('\nA idade dessa pessoa de %d dias expressa em anos,meses e dias e %d anos  %d meses e %d dias ') % (dias,anos,meses,dias1)
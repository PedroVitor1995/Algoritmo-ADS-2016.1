"""21. Leia uma temperatura em Fahrenheit, calcule e escreva a equivalente em Celsius. (tCelsius = (5 * tFahrenheit - 160) / 9)."""

Celsius = input ("Digite a temperatura em Celsius:\n")

Fahrenheit = ((9.0 * Celsius + 160.0) / 5.0)

print ("\nA temperatura de %.2f Celsius em Fahrenheit  e %.2f Fahrenheit") % (Celsius,Fahrenheit)
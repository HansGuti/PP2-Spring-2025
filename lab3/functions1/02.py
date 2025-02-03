def Fahrenheit_to_Celsius(F):
    return round((F - 32) * (5 / 9), 2)
F = float(input('Fahrenheit to Celsius converter: '))
print(Fahrenheit_to_Celsius(F))
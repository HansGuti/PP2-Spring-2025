def Fahrenheit_to_Celsius(F):
    return round((5 / 9) * (F - 32), 2)
F = float(input('Fahrenheit to Celsius Converter: '))
print(Fahrenheit_to_Celsius(F))
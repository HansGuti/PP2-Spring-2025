def fahrenheit_to_celsius(f):
    return round((5 / 9) * (f - 32), 2)
f = float(input('Fahrenheit to Celsius Converter: '))
print(fahrenheit_to_celsius(f))
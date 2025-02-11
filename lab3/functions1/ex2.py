def f_to_c(Fahrenheit):
    return (5 / 9) * (Fahrenheit - 32)

Fahrenheit = float(input("Enter Fahrenheit: "))
centigrade = f_to_c(Fahrenheit)

print(f"{Fahrenheit} Fahrenheit is equal to {centigrade:.2f} centigrades")

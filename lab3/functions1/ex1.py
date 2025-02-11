def gram_to_ounces(grams):
    return grams*28.3495231
grams=float(input("Enter grams:"))
ounces=gram_to_ounces(grams)
print(f"{grams} grams is equal to {ounces:.2f} ounces")
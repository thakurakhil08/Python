letter = "Hey my name is {1} and I am from {0}"
country="India"
name="Akhil"

# print(letter.format(name, country))
print(letter.format(country, name))
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")



# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49.099999))

price = 49.099999
txt = f"For only {price:.2f} dollars!"
print(txt)


print(type(f"{2 * 30}"))
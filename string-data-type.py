#3 Trabajo con el tipo de dato de cadena

# String str
myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Cadenas de entrada
name = input("what is your name? ")
print(name)

# Cadenas de salida
color  = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, your like a {} {}!".format(name, color, animal))
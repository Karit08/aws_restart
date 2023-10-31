"""
Your module description

"""
print("Hello, world")
print("Python has three numeric types: int, float, and complex")
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue)+ " is of the data type " + str(type(myValue)))
myValue1=3.14
print(myValue1)
print(type(myValue1))
print(str(myValue1) + " is of the data type " + str(type(myValue1)))
myValue3=5j
print(myValue3)
print(type(myValue3))
print(str(myValue3) + " is of the data type " + str(type(myValue3)))
myValue4=False 
print(myValue4)
print(type(myValue4))
print(str(myValue4) + " is of the data type " + str(type(myValue4)))
myValue=True
print(myValue)
print(str(myValue) + " is of the data type " + str(type(myValue)))
myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
# name = input("what is your name? ")
# print(name)
# color  = input("What is your favorite color? ")
# animal = input("What is your favorite animal? ")
# print("{}, your like a {} {}!".format(name, color, animal))
myFruitList =["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
myFruitList[2]="orange"
print(myFruitList)
myFinalAnswerTruple=("apple", "banana", "pineapple")
print(myFinalAnswerTruple)
print(type(myFinalAnswerTruple))
print(myFinalAnswerTruple[0])
myFavoriteFuirDictionary={
    "Akua": "apple", 
    "Saanvi": "banana",
    "Paulo": "pineapple"
}
print(myFavoriteFuirDictionary)
print(type(myFavoriteFuirDictionary))
print(myFavoriteFuirDictionary["Akua"])
print(myFavoriteFuirDictionary["Saanvi"])
# 5
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList: 
    print('{} is of the data type {}'.format(item, type(item)))

print(myMixedTypeList[2]);
myMixedTypeList[2] ="nuevo valor"
print(myMixedTypeList[2]);

# 7 if, else, elif
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")


userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")

# 8 while, for in
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
import random 
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
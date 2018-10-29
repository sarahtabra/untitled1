import math
user_choice = int(input("This is a menu-driven program, press 1 for quick pythagoras, press 2 for tip calculator and press 3 for temperature converter.")) #allows the user to choose 1,2 or 3, depending on which program they want to access.
if user_choice == 1:
    print("quick pythagoras")
    a = int(input("enter a value for a")) #allows the user to enter a value for a to eventually calculate what c is.
    b = int(input("enter a value for b")) #allows the user to enter a value for b to eventually calculate what c is.
    c = math.sqrt(a*a + b*b) #calculates the square root for values a & b.
    print ("the value for c is ", c)
if user_choice == 2:
    print("tip calculator")
    total = int(input("what is the value of the total?")) #asks the user to input a value for the total.
    tip = int(input("what tip percent do you want to give?")) #asks the user to input a percentage for tip.
    tip_total = total*(tip/100) #converts the percentage of the tip to a cost.
    print("the amount you're tipping is ", tip_total)
if user_choice == 3:
    print("temperature converter")
    celsius = int(input("enter a temperature for celsius")) #asks the user to input a temperature in celsius.
    fahrenheit = int(input("enter a temperature for fahrenheit")) #asks the user to input a temperature in fahrenheit.
    new_fahrenheit = (celsius*9/5) + 32 #formula to convert celsius to fahrenheit.
    new_celsius = (fahrenheit-32) *5/9 #formula to convert fahrenheit to celsius.
    print("the temperature in celsius is ", new_celsius)
    print("the temperature in fahrenheit is ", new_fahrenheit)
import random
customers = int(input("Welcome to Sarah's Fine Foods! How many people are ordering today?")) #asks the user how many people are ordering.
total_cost = 0
while customers > 3: #ensuring the user doesn't choose over 3 people.
    customers = int(input("That's too many people! Maximum 3 customers, please try again."))
for x in range(0, customers):

    user_choice =(input("Would you like to go shopping for beverages, snacks, or fruits?")) #gives the user three options to shop from.
    if user_choice == "beverages":
            user_choice = (input("Would you like coke, sprite or fruitopia?"))
            if user_choice == "sprite":
                total_cost = total_cost +3 #if the user orders sprite, $3 will be added to the total cost.
                print("This will cost you $3")
            elif user_choice == "coke":
                total_cost = total_cost +4 #if the user orders coke, $4 will be added to the total cost.
                print("This will cost you $4")
            elif user_choice == "fruitopia":
                total_cost = total_cost +2 #if the user orders fruitopia, $2 will be added to the total cost.
                print("This will cost you $2")
    if user_choice == "snacks":
            user_choice = input("Would you like chips, pretzels or cookies?")
            if user_choice == "chips":
                total_cost = total_cost +7 #if the user orders chips, $7 will be added to the total cost.
                print("This will cost you $7")
            elif user_choice == "pretzels":
                total_cost = total_cost +5 #if the user orders pretzels, $5 will be added to the total cost.
                print("This will cost you $5")
            elif user_choice == "cookies":
                total_cost = total_cost +3 #if the user orders cookies, $3 will be added to the total cost.
                print("This will cost you $3")
    if user_choice == "fruits":
            user_choice = input("Would you like strawberries, apples or oranges?")
            if user_choice == "strawberries":
                total_cost = total_cost +8 #if the user orders strawberries, $8 will be added to the total cost.
                print("This will cost you $8")
            elif user_choice == "apples":
                total_cost = total_cost +6 #if the user orders apples, $6 will be added to the total cost.
                print("This will cost you $6")
            elif user_choice == "oranges":
                total_cost = total_cost +5 #if the user orders oranges, $5 will be added to the total cost.
                print("This will cost you $5")


lottery = random.randint(1,10)
if lottery == 7: #every 7th person will win the lottery.
    total_cost = total_cost*0.50 #the calculation to remove 50% from the total cost.
    print("You're the lucky lottery customer! you get 50% off you purchase today!")

lottery2 = random.randint(1,10)
if lottery2 == 5: #every 5th person will win the 500 points worth of store credit.
    print("Congratulations! You just won 500 free store credit points!")
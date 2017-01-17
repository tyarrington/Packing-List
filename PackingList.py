# PackingList.py
# Author: Tinli Yarrington
# Date: 3/11/15, 9/17/15, 1/16/17
# Purpose: print out packing list for user's vacation formatted in a box
# Notes:
#       - add more/less things if traveling by plane/train/boat/car/bus
#       - include whether or not trip is academic-related, leisure, etc.
#       - prevent user from putting in letters when numbers are expected

# method that puts the entire packing list together, takes 6 parameters
def createList(days, temp, swim, formal, rain, gender):
    print("+" * 80)     # printing a line of 80 plus-symbols
    clothing(days, temp, swim, formal, rain, gender)        # calls the clothing method with 5 parameters
    toiletries(days, gender)        # calls the toiletries method with 2 parameters
    miscellaneous()     # calls the miscellaneous method with no parameters
    print("+" * 80)     # printing a line of 80 plus-symbols

# method that generates all the clothing for the packing list, takes 6 parameters
def clothing(days, temp, swim, formal, rain, gender):
    print("| {0:76} |".format("PACKING LIST"))      # print the title "PACKING LIST"

    if temp == 2:       # checks if temp <= 65, which then prints clothes that match the temp it represents
        print("| {0:>5} {1:<70} |".format("-", str(days) + " pairs of shorts/skirts"))
        print("| {0:>5} {1:<70} |".format("-", str(days) + " shirts"))
    else:           # runs when temp is colder (temp > 65)
        print("| {0:>5} {1:<70} |".format("-", str(days) + " pairs of pants"))
        print("| {0:>5} {1:<70} |".format("-", str(days) + " long-sleeves"))
        print("| {0:>5} {1:<70} |".format("-", "boots"))
        if temp == 0:       # checks if temp is much colder (temp <= 40)
            print("| {0:>5} {1:<70} |".format("-", "hat/gloves/scarf"))

    print("| {0:>5} {1:<70} |".format("-", str(days+3) + " sets of underwear"))
    if gender == True:      # checks and runs if user is female and prints accordingly
        print("| {0:>5} {1:<70} |".format("-", str(days+3) + " sets of bras"))

    # prints more clothing
    print("| {0:>5} {1:<70} |".format("-", str(days) + " pairs of socks"))
    print("| {0:>5} {1:<70} |".format("-", "pajamas"))
    print("| {0:>5} {1:<70} |".format("-", "jacket/coat"))
    print("| {0:>5} {1:<70} |".format("-", "sneakers"))
    print("| {0:>5} {1:<70} |".format("-", "casual shoes"))

    if swim == True:        # checks and runs if user is going swimming during vacation
        if gender == True:      # checks if user is female and prints accordingly
            print("| {0:>5} {1:<70} |".format("-", "2 swimsuits"))
            print("| {0:>5} {1:<70} |".format("-", "cover-all"))
        else:       # runs when user is a male
            print("| {0:>5} {1:<70} |".format("-", "2 swim-trunks"))
        print("| {0:>5} {1:<70} |".format("-", "flip-flops"))

    if rain == 2:       # checks if it's raining where the user is going for vacation
        print("| {0:>5} {1:<70} |".format("-", "umbrella/raincoat"))
    elif rain == 1:     # runs if user is not entirely sure if it'll rain there
        print("| {0:>5} {1:<70} |".format("-", "umbrella/raincoat (just in case)"))

    if formal == True:      # checks if user needs formal clothing during vacation
        if gender == True:      # checks if user is female and prints accordingly
            print("| {0:>5} {1:<70} |".format("-", "2-3 sets of formal wear (dresses/skirst, heels, makeup, accessories)"))
        else:       # runs if user is male
            print("| {0:>5} {1:<70} |".format("-", "2-3 sets of formal wear (suits, collar shirts, etc.)"))

# method that generates all the toiletries for the packing list, takes 2 parameters
def toiletries(days, gender):
    print("| {0:>5} {1:<70} |".format("-", "deoderant"))
    print("| {0:>5} {1:<70} |".format("-", "toothbrush"))
    print("| {0:>5} {1:<70} |".format("-", "toothpaste"))
    print("| {0:>5} {1:<70} |".format("-", "shampoo"))
    print("| {0:>5} {1:<70} |".format("-", "conditioner"))
    print("| {0:>5} {1:<70} |".format("-", "body wash"))
    print("| {0:>5} {1:<70} |".format("-", "razor"))
    print("| {0:>5} {1:<70} |".format("-", "lotion"))

    if gender == True:      # checks and runs if user is female and prints accordingly
        print("| {0:>5} {1:<70} |".format("-", "hairbrush/comb"))
        print("| {0:>5} {1:<70} |".format("-", str(days*2) + " pads/tampons"))
        print("| {0:>5} {1:<70} |".format("-", "perfume"))
        print("| {0:>5} {1:<70} |".format("-", "ponytail holders"))
    elif gender == False and days >= 7:     # runs if user is male and is going away for a week or more
        print("| {0:>5} {1:<70} |".format("-", "shaving cream"))

# method that generates some random items for the packing list, takes 0 parameters
def miscellaneous():
    print("| {0:>5} {1:<70} |".format("-", "laptop, charger, and mouse"))
    print("| {0:>5} {1:<70} |".format("-", "phone, headphones, and charger"))
    print("| {0:>5} {1:<70} |".format("-", "books/Kindle"))
    print("| {0:>5} {1:<70} |".format("-", "wallet/money"))
    print("| {0:>5} {1:<70} |".format("-", "random snacks"))

# method that checks if temp will be hot, warm or cold (returns 2, 1, 0 respectively)
def isTemp(temp):
    if temp >= 65:
        return 2
    elif temp >= 40:
        return 1
    else:
        return 0

# method that checks if user will swim during vacation (returns True if they are and False if not)
def isSwimming(swim):
    if swim == "yes":
        return True
    else:
        return False

# method that checks if user will need formal clothing while on vacation (returns True if so and False if not)
def isFormal(fancy):
    if fancy == "yes":
        return True
    else:
        return False

# method that checks if it'll rain while user is on vacation (2 if yes, 1 if they're not sure, and 0 if not)
def isRain(rain):
    if rain == "yes":
        return 2
    elif rain == "idk":
        return 1
    else:
        return 0 

# method that checks the gender of the user (returns True if female and False if male)
def isFemale(gender):
    if gender == "f":
        return True
    else:
        return False

# MAIN METHOD        
def main():
    print("Create your packing list for traveling!")
    print()

    days = 0
    temp = 0
    swim = ""
    fancy = ""
    rain = ""
    gender = ""
    
    while days <= 0:        # continues to cyle through this until user inputs valid answer
        days = eval(input("How many days will you be gone for?   "))        # saves number of days user is traveling into variable "days"
    if days > 7:        # checks and runs if user is going for more than 7 days
        washing = input("Will you wash your clothes while on vacation?   ")        # asks if user will be able to wash clothes while on vacation
        if washing == "yes":        # if the user can wash clothing, then the number of clothing they need to bring is less 
            numWashes = eval(input("How many times will you want to do laundry?   "))
            days = round(days/(numWashes+1))

    temp = eval(input("What is average temperature of where you're going? (in F)   "))     # saves temperature user is traveling to into variable "temp"
    while swim != "yes" and swim != "no":        # continues to cyle through this until user inputs valid answer
        swim = input("Will you be swimming? (put yes or no)   ")        # saves whether or not user is going to swim into variable "swim"
    while fancy != "yes" and swim != "no":       # continues to cyle through this until user inputs valid answer
        fancy = input("Will you need formal-wear? (put yes or no)   ")      # saves whether or not user needs formal clothes into variable "fancy"
    while rain != "yes" and rain != "no" and rain != "idk":       # continues to cyle through this until user inputs valid answer
        rain = input("Will it rain while you're there? (put yes or no or idk)   ")      # saves whether or not it will rain where user is going into variable "rain"
    while gender != "m" and gender != "f":       # continues to cyle through this until user inputs valid answer
        gender = input("Are you a male or a female? (put m or f)   ")        # saves what gender user is into variable "gender"
    print()
    print("Creating the packing list now! ^_^")
    print()

    createList(days, isTemp(temp), isSwimming(swim), isFormal(fancy), isRain(rain), isFemale(gender))       # calls createList method to generate entire list using each variable above, some in called methods, takes 6 parameters 

    print()
    print("Have a wonderful vacation!")

main()      # calls main method

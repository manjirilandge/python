# =======================================================
#            Smart Restaurant Menu & Feedback System     
# =======================================================


customer = input("Enter your name:-")
menu_type = input("Enter youe menu type(veg/n):-")
menu_type = menu_type.lower()

if menu_type == "veg":
    print("Veg menu item is available") 
    food_type = input("Enter your Food Type:-")
    food_type = food_type.lower()
    if food_type == "marathi":
        print("Marathi Food is Available")
    elif food_type == "jain veg food":
        print("Jain veg food is not available")
    elif food_type == "Punjabi food":
        print("Punjabi Food is Available")
    else:
        print("No other veg menu is available")

elif menu_type == "non-veg":
    print("Non-veg menu items are available")
    food_choice = input("Enter your food choice:-")
    food_choice = food_choice.lower()
    if food_choice == "chicken":
        print("chicken is Available")
    elif customer == "mutton":
        print("Mutton is Available")
    elif customer == "egg":
        print("Egg is Available")
    else:
        print("No other non-veg item is available")

#*************** Feedback Section ****************#

feedback = input("Enter Your feedback option:-")
feedback = feedback.lower()

if feedback == "excellent":
    print("Excellent, Thank you for feedback!!")
elif customer == "good":
    print("Good, Thank you for feedback!!")
elif customer == "bad":
    print("bad, Thank you for feedback!")
else:
    print("Thank you for visiting!!")

#========================================================
# Project Description:
# This Python program allows a user (customer) to select
# a food menu (veg/non-veg), choose specific food types,
# and finally give feedback on the experience.
#
# Features:
# - Menu type selection (veg / non-veg)
# - Sub-category food options
# - Availability response
# - Customer feedback handling
#
# Author: Manjiri Landge
# =======================================================
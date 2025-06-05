#********************CONTROL FLOW STATEMENT**************

#if statement:-
a=10
if a<15 :
    print("My name is Manjiri")

#1:-if you want to do not anything after if condition:-\
a=20
if a<25 :
      pass

#if-else statement:-
if 10<3 :
     print("10 is lesser than 3")   #indentation of the if statement
else:
     print("10 is greater than 3")  #indentation of the else statement 

#elif statement:-
#1:-
income=100
if income<50 :
     print("I will able to buy a phone")
elif income<70 :
     print("i will able to buy a car")
elif income<90 :
     print("i will able to buy a house")          
else:
     print("i wont able to buy anything")  
    
                #OR

income=int(input("Enter your income:-"))
if income<50 :
     print("you will able to buy a phone")
elif income<70 :
     print("you will able to buy a car")
elif income<90 :
     print("you will able to buy a house")          
else:
     print("you wont able to buy anything")  

#2:-
total_price=5000
if total_price >20000 :
     discount=total_price*.20
     print("Discount will be:-",discount)
elif total_price <7000 :
     discount=total_price*.05
     print("Discount will be :-",discount)
else:
     print("we won't be able to give any discount")               

               #OR

book=int(input("Enter the book price:-"))
if book>5000 :
     discount=book*.30
     print("Discount on your book will be:-",discount)
elif book<5000 and book>1000 :
     discount=book*.05
     print("The discount on your book will be:-",discount)
else :
     print("We will not able to give you any discount!!")


#3:-
coupen="MANJIRI05"
if coupen=="MANJIRI05" :
     print("You will able to get discount 5%")
     paid_amount=7580-7580*.05
     print("You will be able to get one book with this amount",paid_amount)
else :
     print("Kindly use a valid coupen code")

                 #OR   

coupen=int(input("Enter the coupen:-"))
if coupen=="MANJIRI05" :
     print("You will able to get discount 5%")
     paid_amount=7580-7580*.05
     print("You will be able to get one book with this amount",paid_amount)
else :
     print("Kindly use a valid coupen code")

#4:-
enroll_date = 15
if enroll_date<10 :
     print("You will able to full validity")
elif enroll_date<5 :
     print("You will get only 5 days validity")
else :
     print("You will not get any validity!!")

#5:-
study_hour=(int(input("Enter your Study Hours:-")))
if study_hour>=12 :
     print("You will take 3 months to complete your whole syllabus of MPSC")
elif study_hour>1 & study_hour<12 :
     print("You will tale 6 month to complete your whole syllabus of MPSC")
elif study_hour<1 :
     print("YPu will take 8-9 months to complete your whole syllabus of MPSC")
else :
     print("It will be difficult to complete syllabus of MPSC")


#nested if-elif statement:-
customer=input("Enter your name:-")
menu_type=input("Enter youe menu type(veg/n):-")
menu_type = menu_type.lower()
if menu_type=="veg":
    print("Veg menu item is available") 
    food_type=input("Enter your Food Type:-")
    food_type = food_type.lower()
    if food_type=="marathi":
       print("Marathi Food is Available")
    elif food_type=="jain veg food" :
       print("Jain veg food is not available")
    elif food_type=="Punjabi food" :
       print("Punjabi Food is Available")
    else:
       print("No other veg menu is available")
elif menu_type=="non-veg" :
   print("Non-veg menu items are available")
   food_choice=input("Enter your food choice:-")
   food_choice = food_choice.lower()
   if food_choice=="chicken" :
    print("chicken is Available")
   elif customer=="mutton" :
    print("Mutton is Available")
   elif customer=="egg" :
    print("Egg is Available")
   else:
    print("No other non-veg item is available")

feedback =input("Enter Your feedback option:-")
feedback = feedback.lower()

if feedback=="excellent" :
   print("Excellent,Thank you for feedback!!")
elif customer=="good" :
    print("Good,Thank you for feedback!!")
elif customer=="bad" :
    print("bad,Thank you for feedback!")
else:
    print("Thank you for visiting!!")


#*************** Elif Statement Examples ****************#

#1: Income-based decision
income = 100
if income < 50:
     print("I will able to buy a phone")
elif income < 70:
     print("i will able to buy a car")
elif income < 90:
     print("i will able to buy a house")          
else:
     print("i wont able to buy anything")  

#1 (Alternate): Income-based decision using input
income = int(input("Enter your income:-"))
if income < 50:
     print("you will able to buy a phone")
elif income < 70:
     print("you will able to buy a car")
elif income < 90:
     print("you will able to buy a house")          
else:
     print("you wont able to buy anything")  

#2: Discount based on total price
total_price = 5000
if total_price > 20000:
     discount = total_price * .20
     print("Discount will be:-", discount)
elif total_price < 7000:
     discount = total_price * .05
     print("Discount will be :-", discount)
else:
     print("we won't be able to give any discount")               

#2 (Alternate): Book discount using input
book = int(input("Enter the book price:-"))
if book > 5000:
     discount = book * .30
     print("Discount on your book will be:-", discount)
elif book < 5000 and book > 1000:
     discount = book * .05
     print("The discount on your book will be:-", discount)
else:
     print("We will not able to give you any discount!!")

#3: Coupon validation
coupen = "MANJIRI05"
if coupen == "MANJIRI05":
     print("You will able to get discount 5%")
     paid_amount = 7580 - 7580 * .05
     print("You will be able to get one book with this amount", paid_amount)
else:
     print("Kindly use a valid coupen code")

#3 (Alternate - contains logical issue: comparing int to str, but kept unchanged)
coupen = int(input("Enter the coupen:-"))
if coupen == "MANJIRI05":
     print("You will able to get discount 5%")
     paid_amount = 7580 - 7580 * .05
     print("You will be able to get one book with this amount", paid_amount)
else:
     print("Kindly use a valid coupen code")

#4: Validity based on enrollment date
enroll_date = 15
if enroll_date < 10:
     print("You will able to full validity")
elif enroll_date < 5:
     print("You will get only 5 days validity")
else:
     print("You will not get any validity!!")

#5: MPSC study plan based on study hours
study_hour = (int(input("Enter your Study Hours:-")))
if study_hour >= 12:
     print("You will take 3 months to complete your whole syllabus of MPSC")
elif study_hour > 1 & study_hour < 12:
     print("You will tale 6 month to complete your whole syllabus of MPSC")
elif study_hour < 1:
     print("YPu will take 8-9 months to complete your whole syllabus of MPSC")
else:
     print("It will be difficult to complete syllabus of MPSC")

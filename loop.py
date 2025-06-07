#**********************LOOPING**********************

#To append something in loop
l=["Manjiri", "Landge","Shradha","Patil"]
for i in l :
    print(i+"1")

#To extract each character from String

s="Manjiri"
for i in s :
    print(i)

#For-Else:-It is used to execute after the entire loop is execute
for i in l :
    print(i)
else:
    print("If for loop is going to complete itself then it will comes to else") 

#break :- TO break the entire loop
for i in l:
    if i == "Shradha":
        break
    print(i)
else:
    print("Check this statement.")

            #OR        
for i in s :
    if i == "j" :
        break
    print(i)
else:
    print("Do not execute is unless and untill it is not printing my name.")

#While Loop:- It is used for creating a loop according to some condition
#1:
a=1
while a<10:
    print(a)
    a=a+1

#2
a = 1
while a < 10:
    print(a)
    if a == 5:
        break
    a = a + 1
 
#Continue:- TO give immediate control to the loop
a=1
while a<10:
    print(a)
    a=a+1
    if a==5:
        continue

#To check whether string is palindrome or not
#1:-
s=input("Enter your string:-")
v=s[::-1]
if v==s:
    print("The string is pallindrome")
else:
    print("THe string is not pallindrome")

#To check the key is available in dictionary or not
d={"india":"IND",
   "Canada":"CAN",
   "United State":"US"}

print("india" in d)

#For create a list which is greater then 5 and smaller than 5
l_greater=[]
l_smaller=[]
for i in d:
    if len(i)<=5:
        print(l_smaller.append(i))
    else:
        print(l_greater.append(i))
print(l_smaller)
print(l_greater)

#For check the maximum values in nested dictionary
d1={ "Manjiri": { "a":1,
                  "b":2,
                  "c":3
                 },
      "Rashmi": { "d":4,
                  "e":5,
                  "f":6   
                 }
    }
#To find max value
#1:
lst=[]
for i in d1.values():
    for j in i.values():
        lst.append(j)
        print(lst)
        print(max(lst))
#2:
max=0
for i in d1.values():
    for j in i.values():
        if max<j:
            max=j
    print(max)
#3:
#for i in d1.values():
 #   print(max(d1.values(i)))
for i in d1.values():
    print(max(d1[i].values()))
         
    

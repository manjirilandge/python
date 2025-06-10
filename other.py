#To count number of characters in a string:-
#1:-
s="Manjiri Kishor Landge"
print(len(s))

#2:-
count=0
for i in s:
    count = count+1
    #COUNT +=1
    print(count)

#To reverse a string:-
for i in range(len(s)-1,-1,-1):
    print(s[i])

#by using while loop:-
i=len(s)-1
while(i>=0):
    print(s[i],end="")
    i=i-1

#For finding vowel or not:-
s1="manjiri"
v="AaEeIiOoUu"
for i in s:
    if i in v:
        print ("Vowel",i)
    else:
        print(" not Volwel",i)



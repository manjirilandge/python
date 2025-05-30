# Write a program or Operations of String

#to print a string
a = "Manjiri Landge"
print(a)

#to print type of variable
type(a)


#******This are the INDEXING OPRATIONS******

#To return the character at a specific index
#1:-
a[2]       #It is in the forward direction
#2:-
a[-1]      #It is in the backward direction


#******This are the SLICING OPRATIONS******

#To return the otput in given range
#1:-
a[2:5]      #2 is a starting index and 5 is the end index
a[0:3]
#2:-
a[2:5:1]    #1 is a step size index
a[2:8:2]
#3:-
a[-1:-4]
a[-1:-4:-1]
a[0:-10:-1]
#4:-
a[::]
a[:8]
a[-2:]
a[-2:-1]
#5:-
a[::-1]      #Reverse a String
a[-1::-1]
#6:-
a[-5:5]
a[-5:5:1]


#*******This are the string operator and function******
#To repeat the string in multiple times
#1:-
"Manjiri"*5

#To concatenate two string
#2:-
"Manjiri" + "Landge"

#TO find length of string
#3:-
len(a)

#To find indexed number of character
#4:-
a.find('j')
a.find('an')       #finds the indexed number of combinaton of characters
a.find('xy')       #returns -1 beacuase the combination is not available

#To find the count of occurance of charater in string
#5:-
a.count(a)


#******This are the Split Operation*********

b="Hello, This is Manjiri Landge"

#To split the string
#1:-
b.split()
#To return the type
#2:-
type(a.split())
#To store the Dataset in a  variable
#3:-
l=a.split()
#To acees the dataset from specific index
#1:-
l[3]
l[0:3]
#TO reverse the dataset
l[::-1]
#To split the specific character into the string 
#1:-
l.split('M')      #It return the string in the part in which the given character till not found when the given character is found then from this the dataset will br seperate


#*******This are another different string functions***********

s="hello"
c="HELLO"
d="HeLLo"

#To convert the string into uppercase
#1:-
s.upper()

#To Convert String in lowercase
#2:-
c.lower()

#To swap the string characters from upper to lower or lower to upper
#3:-
d.swapcase()

#To arrange the string in tittle format means the first letter of string is in the uppear case and another are in lowercase
#4:-
s.title()
s.capitalize()     #provide same functions

#To join the string
#5:-
c.join(c)                 #In this each character in string c are printed before the string in s i  different parts
" ".join("Manjiri")        #In this the space will be add in between each character in string

#To reverese a string in another way 
#6:-
for i in ("sudh"):
    print(i)



#*********This are the sstrip Functions**********

m=" Hello "

#To remove space from right side
#1:-
m.rstrip()

#To remove space from left side
#2:-
m.lstrip()

#To remove space from both side
#3:-
m.strip()

#To replace the charaters
#4:-
m.replace("o","i")

#To exapand the string or space 
#5:-
"Manjiri\tLandge".expandtabs()       #1tab = 3space

#To fill the the characters by the given index number
#6:-
m.center(40,'#')        #In this the hello string will be stay in the center and at he both sides # will print until the index 40



#******This are the is function whic returns the condition whether true or false************

e="HELLO MANJIRI"
f="hello manjiri"

#To check given string is in uppercase
#1:-
e.isupper()

#To check given string is in lowercase
#2:-
f.islower()

#To check there is space in between string
#3:-
e.isspace()

#To check the given string in digit
#4:-
e.isdigit()

#To check by given character the string is end or not
#4:-
e.endswith('x')

#To check by given character the string is start or not
#5:-
e.startswith('H')

#To check the given string is in tittle format
#6:-
f.istitle()

#To encode the string using the codec registered for encoding
#7:-
f.encode()



# ******************************
# Basic String Operations
# ******************************

# Declare a string
a = "Manjiri Landge"

# Print the string
print(a)

# Print the type of the variable
print(type(a))


# ******************************
# Indexing Operations
# ******************************


# Forward indexing
print(a[2])     # 'n'

# Backward indexing
print(a[-1])    # 'e'


# ******************************
# Slicing Operations
# ******************************

# Basic slicing
print(a[2:5])     # 'nji'
print(a[0:3])     # 'Man'

# Slicing with step
print(a[2:5:1])   # 'nji'
print(a[2:8:2])   # 'njr'

# Reverse slicing with negative indices
print(a[-1:-4])     # ''
print(a[-1:-4:-1])  # 'egd'
print(a[0:-10:-1])  # ''

# Common slices
print(a[::])        # Full string
print(a[:8])        # 'Manjiri '
print(a[-2:])       # 'ge'
print(a[-2:-1])     # 'g'

# Reversing a string
print(a[::-1])      # 'egdnaL irijnaM'
print(a[-1::-1])    # Same as above

# Edge cases
print(a[-5:5])       # ''
print(a[-5:5:1])     # ''


# ******************************
# String Operators and Functions
# ******************************

# Repeating strings
print("Manjiri" * 5)

# Concatenation
print("Manjiri" + "Landge")

# String length
print(len(a))

# Finding substrings
print(a.find('j'))     # Index of 'j'
print(a.find('an'))    # Index of 'an'
print(a.find('xy'))    # -1 (not found)

# Count of a substring in string
print(a.count("a"))    # Count of 'a' in the string


# ******************************
# Split Operation
# ******************************

b = "Hello, This is Manjiri Landge"

# Split by default whitespace
print(b.split())

# Type of result after split
print(type(b.split()))

# Store split result
l = b.split()

# Accessing elements
print(l[3])        # 'Manjiri'
print(l[0:3])      # ['Hello,', 'This', 'is']
print(l[::-1])     # Reversed list




# Trying to split a list (Error!)
# l.split('M')     # ❌ This will raise an AttributeError


# ******************************
# Other String Methods
# ******************************

s = "hello"
c = "HELLO"
d = "HeLLo"

# Case conversions
print(s.upper())      # 'HELLO'
print(c.lower())      # 'hello'
print(d.swapcase())   # 'hEllO'
print(s.title())      # 'Hello'
print(s.capitalize()) # 'Hello'

# Join operations
print(c.join(c))              # HHELLOEHELLOLHELLOLHELLO
print(" ".join("Manjiri"))    # 'M a n j i r i'

# Another way to reverse a string (character by character)
for i in "sudh":
    print(i)


# ******************************
# Strip and Replace Functions
# ******************************

m = " Hello "

# Strip operations
print(m.rstrip())     # ' Hello'
print(m.lstrip())     # 'Hello '
print(m.strip())      # 'Hello'

# Replace characters
print(m.replace("o", "i"))     # ' Helli '

# Expand tabs
print("Manjiri\tLandge".expandtabs())  # 'Manjiri   Landge'

# Center string with padding
print(m.center(40, '#'))       # '############## Hello ##############'


# ******************************
# Boolean String Methods
# ******************************

e = "HELLO MANJIRI"
f = "hello manjiri"

print(e.isupper())     # True
print(f.islower())     # True
print(e.isspace())     # False
print(e.isdigit())     # False
print(e.endswith('x')) # False
print(e.startswith('H'))  # True
print(f.istitle())     # False

# Encode string (default UTF-8)
print(f.encode())      # b'hello manjiri'

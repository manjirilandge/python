# ******************* TUPLE OPERATIONS IN PYTHON *****************

# Creating tuples
t = ("Manjiri", "Landge", 345, 45+6j, 90.80, True)
t1 = ("Shradha", "Patil", 345, 45+6j, 85.80, False)

# Type checking
print("Type of t:", type(t))
print("Type of t1:", type(t1))

# Slicing operations
print("t1[2:5]:", t1[2:5])            # 345, 45+6j, 85.80
print("t[0]:", t[0])                  # Manjiri
print("t1[-1]:", t1[-1])              # False
print("t1[0::2]:", t1[0::2])          # Every second element

# Reverse order
print("Reversed t:", t[::-1])
print("Reversed t1 (backwards):", t1[-1::-1])

# ❌ t1[0] = "Rushikesh"  # Not allowed — Tuples are immutable

# Concatenating tuples
print("Concatenated tuple:", t + t1)

# Repeating tuples
print("t repeated 5 times:", t * 5)
print("t1 repeated 5 times:", t1 * 5)

# Count the occurrence of an element
print("Count of 345 in t:", t.count(345))

# Finding the index of an element
print("Index of 'Shradha' in t1:", t1.index("Shradha"))

# Tuple with a list inside
t2 = ([22, 33, 444, 55], "Divya", "Gangurde")

# Modifying the list inside the tuple
t2[0][1] = 111  # ✅ Allowed because the list is mutable
print("Modified t2:", t2)

# Converting tuple to list
print("Tuple t:", t)
t_list = list(t)
print("Converted to list:", t_list)

# Converting list back to tuple
t_from_list = tuple(t_list)
print("Converted back to tuple:", t_from_list)

# ----------------------------- RANGE FUNCTION -----------------------------

# 1. Basic range
print("1. Basic range object:")
print(range(6))  # Outputs: range(0, 6)

# 2. Range converted to list
print("\n2. List from range:")
print(list(range(6)))  # Outputs: [0, 1, 2, 3, 4, 5]

# 3. Range with start and end
print("\n3. Range from 4 to 99:")
print(list(range(4, 100)))

# 4. Even numbers using step
print("\n4. Even numbers from 2 to 98:")
print(list(range(2, 100, 2)))

# 5. Invalid reverse range (blank result)
print("\n5. Invalid reverse range:")
print(list(range(4, 10, -1)))  # Outputs: []

# 6. Valid reverse range
print("\n6. Valid reverse range from 10 to 7:")
print(list(range(10, 6, -1)))

# 7. Reverse range with negative step
print("\n7. Reverse range with step -2:")
print(list(range(10, -5, -2)))

# 8. Loop using range
print("\n8. Loop from 0 to 6:")
for i in range(7):
    print(i)

# 9. Loop with negative step
print("\n9. Loop from 10 to -4 with step -2:")
for i in range(10, -4, -2):
    print(i)


# ----------------------- TRIANGULAR PYRAMID PATTERNS -----------------------

# 10. Star pattern using end=""
print("\n10. Triangular pattern using end='':")
n = 10
for i in range(n):
    for j in range(i + 1):
        print("*", end="")  # Default end is '\n', here we override
    print("\n")

# 11. Star pattern with default newline
print("\n11. Triangular pattern with default newline:")
for i in range(n):
    for j in range(i + 1):
        print("*")  # Each * prints on new line
    print("\n")


# ---------------------------- TUPLE EXAMPLES ----------------------------

# Tuple declaration
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# Length of tuple
print("\nLength of tuple:", len(t))

# Range of indexes
print("Index range of tuple:", list(range(len(t))))

# Accessing elements using indexes
print("\nAccessing elements by index:")
for i in range(len(t)):
    print("Index", i, "=", t[i])


# ---------------------- REVERSE TUPLE OPERATIONS -----------------------

# Method 1: Slicing
print("\nReversed tuple using slicing:")
print(t[::-1])

# Method 2: Using reverse range
print("\nReversed tuple using loop:")
for i in range(len(t) - 1, -1, -1):
    print(t[i])


# ---------------------------- DICTIONARY ----------------------------

# Dictionary declaration
d = {
    "a": "Manjiri",
    "b": "Landge",
    "c": 9823292925,
    "d": [91, 2, 3, 4, 5, 6, 7, 8, 9, 0]
}

# 1. Print key-value pairs
print("\nDictionary - key and value:")
for key in d:
    print(key, "=", d[key])

# 2. Print all items inside loop (less ideal)
print("\nDictionary - printing all items inside key loop:")
for key in d:
    print(key, "=", d.items())  # Not recommended

# 3. Best way: using items()
print("\nDictionary - using d.items():")
for key, value in d.items():
    print(key, "=", value)


# ----------------------------- SET EXAMPLES -----------------------------

# Set automatically removes duplicates
s = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0}

print("\nUnique values in set:")
for i in s:
    print(i)

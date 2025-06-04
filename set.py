# *************** SET OPERATIONS IN PYTHON ***************

# Creating a set from a list with duplicate elements
s = [2, 22, 3, 33, 4, 44, 2, 22, 3, 33, 4, 44]
unique_set = set(s)
print("Unique set from list s:", unique_set)

# Type of original 's' (list)
print("Type of s:", type(s))  # Will show list

# Type checking for empty dictionary vs set
s1 = {}           # This is NOT a set, it's a dict
print("Type of s1 ({}):", type(s1))  

s2 = {1, 2, 3}     # This is a set
print("Type of s2 ({1,2,3}):", type(s2))  

# Accessing elements from a set (must convert to list)
l = list(unique_set)
print("Converted set to list:", l)
print("Access first element:", l[0])  # Random, as sets are unordered

# ************ Operations on set ************

s3 = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 77, 7, 88, 8, 99, 9, 90, 0, 0, 9}

# Add operation
s3.add(7)  # No effect since 7 already exists
s3.add("Manjiri")
# s3.add([1,2,3,4])  # ❌ Error: list is unhashable
s3.add((1,2,3,4,5,6,7,8,9,0))  # ✅ Tuple is hashable

print("Set after add operations:", s3)

# Remove operation
s3.remove(4)   # Removes 4
# s3.remove(50)  # ❌ Error if 50 not present
print("After removing 4:", s3)

# Discard operation (no error if item not present)
s3.discard(2)  # Removes 2 if present
s3.discard(100)  # No error even if 100 not in set
print("After discard operations:", s3)

# Case sensitivity in sets
s4 = {"manjiri", "Manjiri"}
print("Case sensitive set:", s4)

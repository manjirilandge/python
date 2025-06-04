# ******************** LIST OPERATIONS DEMO ********************

# 1. Create a List
l = ["Manjiri", "Landge", 9270012905, 45+6j, True, 90.80]
print("Original List:", l)

# 2. Data Type
print("Type of l:", type(l))

# 3. Indexing
print("l[1]:", l[1])           # "Landge"
print("l[-1]:", l[-1])         # 90.80

# 4. Slicing
print("l[0:5]:", l[0:5])       # First 5 elements
print("l[-1:6]:", l[-1:6])     # Empty due to direction

# 5. Access Nested Elements
print("Second character of l[0]:", l[0][1])  # "a"
print("Real part of complex number:", l[3].real)
print("Imaginary part of complex number:", l[3].imag)

# 6. Concatenate Lists
l1 = ["Shardha", "Patil", 699319253, 45+6j, 85.90]
print("Concatenated List:", l1 + l)

# l1 + "sudh" --> Invalid
# l1 + ["sudh"] --> Valid
print("Concatenation with single-element list:", l1 + ["sudh"])

# 7. Repetition
print("Repeated l1 5 times:", l1 * 5)




# 8. Mutability - Replace element
l1[0] = "Kunal"
print("Modified l1:", l1)

# 9. Length of Lists
print("Length of l1:", len(l1))
print("Length of l:", len(l))

# 10. Membership Testing
print("'Manjiri' in l:", 'Manjiri' in l)
print("'Patil' in l1:", 'Patil' in l1)
print("345 in l1:", 345 in l1)

# 11. Extra Indexing (reversed range)
print("Reversed slice (invalid):", l[-1:6:-1])
print("Reversed slice (valid):", l[5:2:-1])

# 12. Append Elements
l1.append(44.4)


l.append("Manjiri")
print("After append l1:", l1)
print("After append l:", l)

# 13. Remove Elements
print("Popped from l1:", l1.pop())
print("Popped index 1 from l1:", l1.pop(1))
print("l1 after pop operations:", l1)

# 14. Insert Elements
l.insert(1, "kishor")
l1.insert(1, "Bhausaheb")
print("l after insert:", l)
print("l1 after insert:", l1)

# 15. Reverse List
print("Reversed l1 by slicing:", l1[::-1])
print("Reversed l1 (same as above):", l1[-1::-1])

l.reverse()
l1.reverse()
print("l after reverse() method:", l)
print("l1 after reverse() method:", l1)

# 16. Count Elements
print("Count of 'Manjiri' in l:", l.count("Manjiri"))
print("Count of 'patil' in l1 (case sensitive):", l1.count("patil"))

# 17. Extend List
l1.extend([2, 3, 4, 5, 6, 7])
l.extend([22, 333, 4444, 55555])
print("Extended l1:", l1)
print("Extended l:", l)

# 18. Tabs and Formatting
print("Expanded Tabs Example:")
print("Manjiiri\tLandge\tkishor".expandtabs())

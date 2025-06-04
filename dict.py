#************DICTIONARY****************

# Create a dictionary
d = {"key1": "Manjiri", 'key2': 45, 22: [3, 4, 5, 6]}
print(d)
print(type(d))

# Access values by keys
print(d["key1"])
print(d['key2'])
print(d[22])

# Duplicate keys
d2 = {"key1": "Manjiri", "key1": "Landge"}
print(d2["key1"])  # Output: Landge

# Extra examples
d3 = {"+++": "venu"}
print(d3)

d4 = {
    "name": "Manjiri",
    "mob_no": 9270012905,
    "e_mail": "landgemanjiri@gmail.com",
    "list": [1, 2, 3, 4, 5],
    "tuple": (1, 2, 3, 4, 5, 6),
    "set": {1, 2, 3, 4, 5, 6},
    "dict": {1: 22, 2: 33, 3: 44}
}
print(d4)
print(type(d4["list"]))
print(d4["tuple"])
print(d4["list"][2])
print(d4.keys())
print(d4.values())
print(d4.items())
print(type(d4.items()))

# Add new key
d4["string"] = "Manjiri"
print(d4)

# Update a key
d4["list"] = [2, 3, 4, 5, 6]
print(d4)

# Delete a key
del d4["list"]
print(d4)

# Use .get()
print(d4.get("name"))

# Combine dictionaries
d.update(d4)
print(d)

# Append list to itself (just example)
l = [1, 2, 3, 45]
l.append(l)
print(l)

# Tuple index
t1 = ("Manjiri", 45+6j, 1, True)
print(t1.index(True))

# fromkeys example
key = ("name", "age")
values = ("Manjiri", 18)
d7 = dict.fromkeys(key, values)
print(d7)

# Count value "Manjiri" in dictionary values
print(list(d4.values()).count("Manjiri"))

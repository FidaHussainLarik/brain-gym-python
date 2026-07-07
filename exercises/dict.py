#Counting names appearence in a dictionary
counts = dict()

names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia", "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona","Hannah", "Ian", "Julia", 
"Bob", "Charlie", "Diana", "Fiona", "George", "Hannah", "Ian", "Julia", "Alice"]


# Short method of couting values in a dictionary
for name in names:
    counts[name] = counts.get(name,0) + 1

name = 'Fida Hussain'
# get() method retrun the value of key if it exist , if not a default value is returned
print(counts.get(name,None))

# Extracting keys and values in form of list from a dictionary
keys = list(counts.keys())
values = list(counts.values())
items = list(counts.items())



print("Keys   : ",keys)
print("Values : ",values)
print("Items  : ",items)

# Walking through a dictionary
for key, value in counts.items():
    print(f"{key}: {value}")



# Lengthy method of couting values in a dictionary
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1



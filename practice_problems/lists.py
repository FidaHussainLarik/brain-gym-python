
friends = ['Fida','Bob','Alice','Charle']

# for friend in friends:
#     print(friend)

    
# range function return a list of values start from 0 upto n-1
# list1 = list(range(5))
# print(list1)

# COncatenation
list1 = [1,2,3]
list2 = [4,5,6]

list3 = (list1+list2)

# values greater then 2
list4 = list3[2:]
# print("List 4: ",list4)

#Print all list methods
# print(dir(list))

# if 3 in list4:
#     print("3 is present in the list")


# IN opeartor
# if 20 not in list4:
#     print("20 is not in the list")

# print(20 not in list4)


# Computing average of user's entered values
"""
count = 0
total = 0
while True:
    value = input("Enter a number: ").lower().strip()
    if value == 'done':
        break
    value = float(value)
    total = (total+value)
    count = count+1


average = (total/count)
print(f"Total values entered by you: {count}")
print(f"Average : {average}")
"""

# Creating an empty list()

"""
numslist = list()

while True:
    value = input("Enter a number: ").lower().strip()
    if value == 'done':
        break

    try:
        value = float(value)
        numslist.append(value)
    except:
        print("Enter a valid number!")
        continue
average = sum(numslist) / len(numslist)
print(f"Total values entered by you: {len(numslist)}")
print(f"Average : {average}")
"""



# Strings and Lists
# Converting strings into lists

line = 'a lot of spaces'
list1 = line.split()
print(list1)

line  = 'first,second,third,fourth'
list1 = line.split(',')
print(list1)

# No delimeter/perimeter is assigned to split() function that's why it take ' ' space as a delimeter. But their is no any space in between values so string is converted into a single item list.

line  = 'first,second,third,fourth'
list1 = line.split()
print(list1)


    
list1 = [2,3,4,5,6]
print("Maximum: ",max(list1))
print("Minimum: ",min(list1))

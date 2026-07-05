print("______________________________________Working with file______________________________________\n")



# Reading file named 'ai_engineer_role.txt'

my_file = open('ai_engineer_role.txt','r')
count = 0

for line in my_file:
    count = count+1
    print(line)



print("Counting lines in a file")
print(f"There are {count} lines in my file 'ai_engineer_role.txt'")


print("\n______________________________________Working with file______________________________________")
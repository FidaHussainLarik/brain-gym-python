print("*" *100)
print("                               Working with Files                        ")
print("*" *100)
# Reading file named 'ai_engineer_role.txt'

print("\n" + "-" * 60)
print("File Content")
print("-" * 60)



file_handle = open('ai_engineer_role.txt','r')

count = 0
for line in file_handle:
    count = count+1

# Reset file pointer to the beginning
file_handle.seek(0)
content = file_handle.read()
print(f"Total lines in file    :  {count} ")
print(f"Length in words of file:  {len(content)}")



file_handle.seek(0)
content = file_handle.read()
print("Content of the file    :")
print(content)
 

# Printing first 20 characters of the file
print("\n\nSubstring of first 20  characters from the file: ",content[:20])

# Searching the file
user_input = input("Enter what you want to search: ")


# Reset file pointer to the beginning
file_handle.seek(0)

print(f"🔍 in the file  for {user_input}: ")
for line in file_handle:
    if line.startswith(user_input):
        print(f"Line containing [ {user_input} ]: ")
        print(line)


print("*" *100)
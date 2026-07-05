print("*" *100)
print("│                                 Working with Files                        ")
print("*" *100)



# Reading file named 'ai_engineer_role.txt'

print("\n" + "-" * 60)
print("File Content")
print("-" * 60)



file_handle = open('ai_engineer_role.txt','r')
count = 0

for line in file_handle:
    count = count+1
    # print(line)

# Counting lines in a file
print("Counting lines in a file")
print(f"There are {count} lines in my file 'ai_engineer_role.txt'")




# Priting  the whole file in a single string
# Reset file pointer to the beginning
file_handle.seek(0)

print("\nPriting  the whole file in a single string:\n")
content = file_handle.read()
print(content)
print(f"Length {len(content)}") 


# Printing first 20 characters of the file
print("\n\nSubstring of first 20  characters from the file: ",content[:20])

print("*" *100)

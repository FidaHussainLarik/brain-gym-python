print("*" *100,"\n")

file_handle = open('ai_engineer_role.txt')

for line in file_handle:
    # Removing free lines from the text file
    line = line.strip()
    if line.startswith('Beyond'):
        print(line)


print()
print("*" *100)
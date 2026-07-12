 # File used: ai_engineering_role.txt

fname = input("Enter the file you want to work on: ")

try:
    file_handle = open(fname)
except:
    print("File not found!")
    quit()

count = 0
for line in file_handle:
    line = line.rstrip()
    if line.startswith("Beyond"):
        print(line)
        count = count+1
print(f"There are {count} lines in the file")


file_handle.close()
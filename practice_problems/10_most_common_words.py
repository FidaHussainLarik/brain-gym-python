"""
Write a program to print top 10 most common words

"""
try:
    file_handle = open('romeo.txt')

    for line in file_handle:
        print(line)

except FileNotFoundError:
    print("File not found")
    
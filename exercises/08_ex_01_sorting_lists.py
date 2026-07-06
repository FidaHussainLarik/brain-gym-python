"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt

"""

file_name = input("Enter file name: ").strip().lower()

try:
    file_handle = open(file_name)
except:
    print("File 'romeo.txt' not found!")
    # Exit the program
    quit()


content = file_handle.read()
lst_words = list()
lst_words = content.split()

# Empty list for storing distinct values
words_copy = list()


for word in lst_words:
    if word not in words_copy:
        words_copy.append(word)

words_copy.sort()

print(words_copy)
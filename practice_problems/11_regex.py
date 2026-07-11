from pathlib import Path
import re

DATA_FILES_DIR = Path(__file__).resolve().parent.parent/"data"


# for clear visualization this seperator method is best to use
def border():
    print(70*'-')

try:
    file_handle = open(DATA_FILES_DIR/'mbox-short.txt')
except FileNotFoundError:
    print("File not found!")
    quit()


""""    Using re.search() like find()   """

# print(70 * '-')
# print("Finding the matched lines from the file using find()")
# print(70 * '-')

# for line in file_handle:
#     if line.find('From: ') >= 0:
#         print(line.rstrip())


# file_handle.seek(0)

# print(70 * '-')
# print("Finding the matched lines from the file using re.search()")
# print(70 * '-')

# for line in file_handle:
#     if re.search('From: ',line):
#         print(line.rstrip())

# print(70 * '-')
# if None:
#     print("Behaviour of if with None")
# else:
#     print("None is considered as a false value inside if block")
# print(70 * '-')



# file_handle.seek(0)


"""     Using search() like startwith()     """

# print(70 * '-')
# print("Finding the matched lines from the file using re.startwith()")
# print(70 * '-')

# for line in file_handle:
#     line = line.rstrip()
#     if line.startswith('From: '):
#         print(line)

# print(70 * '-')
# print("Finding the matched lines from the file using re.search('^From: ',line)")
# print(70 * '-')

# # Moves cursor of file to the start of the line
# file_handle.seek(0)

# for line in file_handle:
#     line = line.rstrip()
#     # re.search('^From: ',line) return True if line begins with From:, else returns false
#     if re.search('^From: ',line):
#         print(line)


"""        Wild-Card character '.'         """

# print(70 * '-')
# print("Wild-Card character '.' ")
# print(70 * '-')

# count = 0
# for line in file_handle:
#     line = line.rstrip()
#     # re.search('^X.*:',line) return True if line begins with X contains zero or many characters inside followed by :
#     if re.search('^X.*:',line):
#         print(line)
#         count = count + 1
# print("Number of matched line is: ",count)


# print(70 * '-')
# print("Fine-Tuning our matched data")
# print(70 * '-')

"""
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Sat Jan  5 09:14:16 2008
X-DSPAM-Confidence: 0.8475
X-DSPAM-Probability: 0.0000

Extracting only the line like above

Ignoring:
X DSPAM Probability: 0.0000

# """
# file_handle.seek(0)
# count = 0
# for line in file_handle:
#     line = line.rstrip()
#     # re.search('^X-/S*:',line) return True if line begins with X- contains one or more non-blank characters followed by a ':'
#     if re.search("^X-\S+:",line):
#         print(line)
#         count = count + 1

# print(f'Count of these fine tuned lines should be : {count}')




"""     Matching and extracting data        """
# y = list()

# x = """The findall method extract all the digit data from this line and store them in a list.
#     1 will be xtracted first then 2, f3, 4, and 5
#     and this is a multil6ine st7ring
# """
# border()
# y = re.findall('[0-9]+',x)
# print('List of numbers (in form of string) extracted from the text/string: ',y)





# # Uppercase vowels in string
# border()
# Upper_case = re.findall('[fh]+',x)
# print(Upper_case) 
# print(type(Upper_case))
# border()



"""     Greedy Matching        """
# x = "From: Using the: Character: Greedy: "
# border()
# # this greedly searches for all occurances of :
# y = re.findall("^F.+:",x)
# print(y)


# # Removing greedyness

# # this greedly searches for all occurances of :
# y = re.findall("^F.+?:",x)
# print(y)

# border()

"""    Fine-Tune String Extraction       """

# border()
# for line in file_handle:
#     line = line.rstrip()

#     # Extract email address of the sender in a quite smart way ["\\S+@\\S+"]
#     # \\S --> means non-blank character
#     # \\+@ followed by a '@'
    
#     if re.findall("^From: ",line):
#         email = re.findall("\\S+@\\S+",line)
#         # print(email[0])


# # Alternative method to do this same
# file_handle.seek(0)

#     #"^From: (\\S+@\\S+)" --> Searches for the line containing From: in the begining
#     # But extract email address of the sender in a quite smart way ["\\S+@\\S+"]
#     # \\S --> means non-blank character
#     # \\+@ followed by a '@'

for line in file_handle:
    line = line.rstrip()
    email = re.findall("^From (\\S+@\\S+)",line)

    if email:
        print(email[0])

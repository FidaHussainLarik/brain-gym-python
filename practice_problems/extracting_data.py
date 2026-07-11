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


for line in file_handle:
    line = line.rstrip()

#     #"^From: (\\S+@\\S+)" --> Searches for the line containing From: in the begining
#     # But extract email address of the sender in a quite smart way ["\\S+@\\S+"]
#     # \\S --> means non-blank character
#     # \\+@ followed by a '@'
    
    # email = re.findall("^From (\\S+@\\S+)",line)        
    # print(email)

x = "From gsilver@umich.edu Fri Jan  4 11:11:52 2008"    
email = re.findall('^From (\\S+@\\S+)',x)
print(email[0])
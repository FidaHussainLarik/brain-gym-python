import re

try:
    file_handle = open('mbox-short.txt')

    for line in file_handle:
        if line.find('From: ') >= 0:
            print(line) 

except:
    print("File not found!")

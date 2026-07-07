# File used 'mbox-short.txt'

"""

9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

file_name = input("Enter file:")
if len(file_name) < 2:
    file_name = "mbox-short.txt"

senders = dict()

try:
    file_handle = open(file_name)
    for line in file_handle:
        if not line.startswith('From '):
            continue
        words = line.split()
        if len(words) > 1:
                senders[words[1]] = senders.get(words[1],0) + 1
    mass_sender = None
    greatest_count = 0

    for word, count in senders.items():
        if word is None or count > greatest_count:
            mass_sender = word
            greatest_count = count

    print(mass_sender,greatest_count)

except FileNotFoundError:
    print("File not found!")
    quit()

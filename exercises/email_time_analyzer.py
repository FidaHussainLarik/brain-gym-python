
"""

10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

"""
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


file_name = input("Enter file:")

try:

    file_handle = open(DATA_DIR / file_name)

    # 'hour' stores hours only
    # 'time' stores hours, minute and seconds
    hour = str()
    time = list()
    hours_count = dict()
    
    for line in file_handle:
        if not line.startswith('From '):
            continue

        words = line.split()
        time = words[5].split(':')
        hour = time[0]

        if len(words) >= 1:
            hours_count[hour] = hours_count.get(hour, 0) + 1

    for (key,value) in sorted(hours_count.items()):
        print(key,value)

except FileNotFoundError:
    print("File not found!")
   
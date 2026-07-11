
from pathlib import Path
import re
DATA_PATH = Path(__file__).resolve().parent.parent/'data'
file_handle = open(DATA_PATH/'mbox-short.txt')

# Stores spam confidence numbers
numlist = list()

for line in file_handle:
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
    if stuff:
        if len(stuff) != 1: continue
        num = float(stuff[0])
        numlist.append(num)
        print(stuff)
print("Maximum Spam Confidence: ",max(numlist))
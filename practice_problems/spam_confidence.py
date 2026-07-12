
from pathlib import Path
import re
DATA_PATH = Path(__file__).resolve().parent.parent/'data'
file_handle = open(DATA_PATH/'mbox-short.txt')

# Stores spam confidence numbers
numlist = list()

for line in file_handle:
    line = line.rstrip()
    # Look for the line 'X-DSPAM-Confidence: ' and extact the numeric part from it
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
    if stuff:
        # If stuff contains more then one float value ignore it and continue
        if len(stuff) != 1: continue
        # Number extracted from the line is added to numlist
        num = float(stuff[0])
        numlist.append(num)
        print(stuff)
print("Maximum Spam Confidence: ",max(numlist))


file_handle.close()
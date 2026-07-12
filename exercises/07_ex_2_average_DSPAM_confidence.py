
# Note: File used in this program: mbox-short.txt

# 7.2 Write a program that prompts for a file name, then opens that file 
# and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475

from pathlib import Path
DATA_PATH = Path(__file__).resolve().parent.parent/"data"

fname = input("Enter file name: ")

# We add '../data/' to the filename to access it from the /exercises folder
try:
    file_handle = open(DATA_PATH/fname)
except FileNotFoundError:
    print(f"File '{fname}' not found in the data folder.")
    quit()

count = 0
total = 0

for line in file_handle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        # Find the colon and slice the string to get the number
        start_indx = line.find(':')
        number_str = line[start_indx + 1:].strip()
        
        # Convert to float and add to our tracking variables
        numeric_value = float(number_str)
        total = total + numeric_value
        count = count + 1

# Calculate and print the average
if count > 0:
    print(f"Average spam confidence: {total / count}")
else:
    print("No lines found with X-DSPAM-Confidence")


file_handle.close()
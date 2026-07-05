"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475

1. Count these lines 
2. extract the floating point values from each of the lines and 
3. compute the average of those values and produce an output as shown below.
 
Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

fname = input("Enter file name: ")

try:
    file_handle = open(fname)
except:
    print("File not found!")
    quit()

count = 0
total = 0

for line in file_handle:
    
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        start_indx = line.find(':')
        start_indx = str(start_indx).strip()
        start_indx = int(start_indx)

        numeric_value = float(line[start_indx+1 : ])
        total = total + numeric_value
        count = count+1

print(f"Average spam confidence: {total/count}")
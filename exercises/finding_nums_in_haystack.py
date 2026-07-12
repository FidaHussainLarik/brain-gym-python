
import re
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent/"data"

def border():
    print(70*'-')


try:
    file_handle = open(DATA_PATH/"regex_sum.txt")
except FileNotFoundError:
    print("File not found ⚠")
    quit()

num_list = list()

for line in file_handle:
    # Extract number from each line. Line may contains list of zero or many numbers
    extracted_nums =  re.findall('[0-9]+',line)

    # When no num is found skip that iteration
    if not extracted_nums: 
        continue

    for num in extracted_nums:
        num = int(num)
        # Adding them into a list of numbers
        num_list.append(num)
print(f"Sum: {sum(num_list)}")


file_handle.close()

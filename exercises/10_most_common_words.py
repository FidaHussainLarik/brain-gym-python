"""
Write a program to print top 10 most common words

                Algorithm

                Read file
                    ↓
                Split each line into words
                    ↓
                Count words using dictionary
                    ↓
                Convert dictionary to (count, word) tuples
                    ↓
                Sort descending
                    ↓
                Print first 10

"""

from pathlib import Path
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

try:
    
    file_handle = open(DATA_DIR / "romeo.txt")

    counts = dict()

    for line in file_handle:
        words = line.split()
        # count the words using dictionary
        for word in words:
            word = word.lower()
            counts[word] = counts.get(word,0) + 1            

    #Converting dictionary items into a list of tuples so we can sort them based on their values
    sorted_tup_list = list()
    for (key,value) in counts.items():
        sorted_tup_list.append((value,key))

    sorted_tup_list = sorted(sorted_tup_list,reverse=True)
    count = 0
    for tup in sorted_tup_list[:10]:
        print(f"{(count+1)}: {tup}")
        count = count + 1
    file_handle.close()

except FileNotFoundError:
    print("File not found")
    

from pathlib import Path
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

counts = dict()

try:
    file_handle = open(DATA_DIR/'words.txt')

    for line in file_handle:
        print(line)
        words = line.split()
        print(words)
        for word in words:
            counts[word] = counts.get(word,0) + 1

    bigword = None
    bigcount = 0
    for word, count in counts.items():
        if word is None or count > bigcount:
            bigword = word
            bigcount = count

    print(f"Big word : {bigword}")
    print(f"Big count: {bigcount}")

    
    file_handle.close()

except FileNotFoundError:
    print("File not found!")
    quit()
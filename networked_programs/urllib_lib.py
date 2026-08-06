import urllib.request, urllib.parse, urllib.error

file_handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

print()

counts = dict()

for line in file_handle:
    line = line.decode().strip()
    words = line.split()

    for word in words:
        counts[word] = counts.get(word,0) + 1

    print(line)


print("DICTIONARY OF WORDS")
tup_list = list()
for key, val in counts.items():
    tup_list.append((val,key))

tup_list.sort(reverse=True)

for val, key in tup_list:
    print(key,val)
print()
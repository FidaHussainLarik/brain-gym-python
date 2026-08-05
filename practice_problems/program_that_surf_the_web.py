import urllib.request, urllib.parse, urllib.error

file_handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


print()
counts = dict()

for line in file_handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1


sorted_tup_list = list()

for (key,value) in counts.items():
    sorted_tup_list.append((value,key))

sorted_tup_list.sort(reverse=True)
for key,value in sorted_tup_list:
    print(key,value)

print()
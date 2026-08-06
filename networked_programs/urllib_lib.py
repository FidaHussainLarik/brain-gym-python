import urllib.request, urllib.parse, urllib.error

file_handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

print()

for line in file_handle:
    line = line.decode().strip()
    print(line)

print()
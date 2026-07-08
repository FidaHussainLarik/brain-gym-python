d = {'b':1, 'c': 22, 'a':10}

tup_list = sorted(d.items())

print(tup_list)

temp_list = list()

for (k,v) in d.items():
    temp_list.append((v,k))
temp_list = sorted(temp_list)
print(temp_list)



print(type(temp_list))

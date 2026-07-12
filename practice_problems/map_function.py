nums = ["1", "2", "3"]

print(nums)


"""
        working of map()
        map(int, nums)

"10"  ---> int() ---> 10

"20"  ---> int() ---> 20

"30"  ---> int() ---> 30


    returns a list of numbers


"""

result = map(int, nums)


# print(list(result))



# enumerate
students = ["Ali", "Sara", "Ahmed"]

for index, student in enumerate(students,start=1):
    print(index, student)
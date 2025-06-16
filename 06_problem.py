from functools import reduce

# l = [5, 10, 25, 3, 8]
# largest = l[0]
# for i in l:
#     if i > largest:
#         largest = i
# print(f"largest number in the list is {largest}")

"""Using reduce"""
l = [5, 10, 25, 3, 8]
largest = reduce(lambda a,b: a if a>b else b,l)
print(largest)
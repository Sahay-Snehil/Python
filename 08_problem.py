n = input("Enter first word: ")
n_2 = input("Enter second word: ")

n_list = list(n)
n_list.sort()
print(n_list)



n_2list = list(n_2)
n_2list.sort()
print(n_2list)



if n_list == n_2list:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams!!")


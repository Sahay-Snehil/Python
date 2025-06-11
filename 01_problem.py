"""Check if a given string is a palindorme """

n = int(input("Enter any number: "))
n_str = str(n)

rev_str = n_str[::-1]
if n_str == rev_str:
    print("Number is palindrome")
else:
    print("Number is not a palindrome")

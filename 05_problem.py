n = input("Enter any word ")

vowels = "aeiou"
count = 0

for i in n.lower():
    if i in vowels:
        count += 1
print(f"Number of vowels in {n} is {count}")

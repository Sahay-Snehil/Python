# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# n= int(input("Enter any number: "))
# print(factorial(n))

"""Without Functions"""
 
n = int(input("Enter any number: "))
product = 1

if n == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        product *= i
        i       += 1
    print(f"Factorial of {n} is {product}")

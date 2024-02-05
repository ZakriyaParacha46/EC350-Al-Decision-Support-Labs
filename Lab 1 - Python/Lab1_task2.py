##task 2 
def fact(n):
    if (n<1):return 1
    return n*fact(n-1)

num = int(input("Enter a number: "))
print(f"Factorial {num} : {fact(num)}")


def fib(num):
    a,b= 1,1
    for i in range(num):
        temp= b
        b+= a
        a= temp
    return b

num= int(input("Enter a number: "))
print('Num: ', fib(num) )
##task1
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
    
func = {1: add , 2:subtract ,3:multiply, 4:divide}
while(True):
    choice= int(input("Enter choice ie\n1- add\n2- subtract\n3- Multiply\n4- divide\n5- Exit\n? "))
    if(choice==5):break
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    print("Result",func[choice](a,b))
    
def addition(a,b):
    return a+b
def subraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b == 0:
        return "division by 0 not allowed"
    return a/b
def calculator():
    print("Select Operation!!")
    print("1.Addition")
    print("2.Subraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter your choice from 1,2,3,4? "))
    if choice not in ['1,2,3,4']:
        print("Invalid choice")
        return
    a = int(input("Enter First Number? "))
    b = int(input("Enter Second Number? "))

    if choice == 1:
        print(addition (a,b))  
    elif choice == 2:
        print(subraction(a,b))
    elif choice == 3:
        print(multiplication(a,b))
    elif choice == 4:
        print(division(a,b)) 
    
               
        
calculator()                        
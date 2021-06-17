def sum():
    result = first+second
    return result
def sub():
    result= first-second
    return result
def mul():
    result= first*second
    return result
def div():
    result= first/second
    return result

while True:
    print("------*** CALCULATOR ***----------\n")
    choice = int(input("Choice which operation you want to do?\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Exit\nYour choice: "))

    if choice==1:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        print(sum())
       
    elif choice==2:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        print(sub())
     
    elif choice == 3:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        print(div())
      
    elif choice==4:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        print(mul())
       
    else:
        print("Thank you come again!")
        break

def task_1():
    password = "Password123"
    guess = str(input("Enter your password: "))

    while guess != password:
        print("Password incorrect, try again!")
        break
        
    else:
        print("Password cracked!")
        
def task_2(): # Times table

    number1 = int(input("Enter a number to multiply: "))
    number2 = int(input("Enter the number of times you wish to multiply the previous number: "))
    count = 1
    
    while count <= number2
        print(f"{count} x {number1} = {number2 * number 1}")
        count += 1


def task_3(): # Count mississippis
 
 count = 1

 while count < 6:
    print(f"{count} mississippi")
    count += 1
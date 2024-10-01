def task_1():
    password = "Password123"

    # Enter your code here
    guess = ""
    
    while guess != password:
        print("Enter password: ")
        guess=input()
    else:
        print("password granted!")
    

def task_2(): # Times tables
    # Enter your code here
counter = 1
timetables_1 = int(input("Enter a number: "))
timetables_2 = int(input("Enter another number: "))

while counter <= timetables_1:
    print(f"{timetables_1} * {counter} = {timetables_1 * counter}")
    counter += 1

    
    
def task_3(): # Count mississippis
import time 

counter = 1

while counter <= 5:
    print(f"{counter} Mississippi")
    time.sleep(1)
    count += 1



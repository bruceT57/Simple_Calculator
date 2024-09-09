import sys

def calculation(choice,firstNum,secondNum):
    match choice:
        case 1:
            return float(firstNum + secondNum)
        case 2:
            return float(firstNum - secondNum)
        case 3:
            return float(firstNum * secondNum)
        case 4:
            return float(firstNum / secondNum)
        case _:
            print("Invalid Operation! Calculator will Exit.")
            sys.exit()

while True:
    try:
        num1 = float(input("Please Enter the First Number: "))
        num2 = float(input("Please Enter the Second Number: "))
        userChoice = int(input("Please Select your Operation: \n "
                   "1.Add \n 2.Subtract \n 3.Multiple \n 4.Divide \n"
                   "User Operation: "))
        print("Calculation Result is: ",calculation(userChoice,num1,num2))
        sys.exit()
    except ValueError:
        print("Invalid Input! Calculator will Exit.")
        sys.exit()
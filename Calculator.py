print("What type of math are you doing?")
print("Press 1 for arithmetic. Examples include addition, subtraction, multiplication, and division problems.")

mathType = input()

def selectMath(mathType):
    if mathType == 1:
        print("You have chosen to do arithmetic.")
        print("Press 1 for addition")
        arithmeticType = input()
        
selectMath(mathType)

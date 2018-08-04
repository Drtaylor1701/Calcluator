MathType = 0
equation = 0
def main():
  print("Welcome to Calculator!")
  selectMathType()
  basicArithmetic()

def selectMathType():
    type = input("For arithmetic press 1. For geometry press 2. For measurement press 3. ")
    if type == 1:
        MathType = Arithmetic
    elif type == 2:
        MathType = Geometry
    elif type == 3:
        MathType = Measurement

def basicArithmetic():
    print("Please enter the first number in the equation. ")
    firstNumber = input()
    print("Please enter the second number in the equation. ")
    secondNumber = input()
    print("What operation are we doing? ")
    print("Input + for addition, - for subtraction, * for multiplication, and / for division. ")
    operation = input()
    if operation == "+":
        equation = firstNumber + secondNumber
    elif operation == "-":
        equation = firstNumber - secondNumber
    elif operation == "*":
        equation = firstNumber * secondNumber
    elif operation == "/":
        equation = firstNumber * secondNumber

    print(equation)
    return equation


if __name__== "__main__":
  main()

MathType = ""
def main():
  print("Welcome to Calculator!")
  selectMathType()

def selectMathType():
    type = input(For arithmetic press 1. For geometry press 2. For measurement press 3.)
    if type == 1:
        MathType = Arithmetic
    elif type == 2:
        MathType = Geometry
    elif type == 3:
        MathType = Measurement
    else:
        print("That is not a recognized math type at this time.")

if __name__== "__main__":
  main()

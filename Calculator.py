
def arithmetic(first, second, operation):
    first = float(first)
    second = float(second)
    if operation == 1:
        total = first + second
        return total

print("What type of math are you doing?")
print("Press 1 for arithmetic. Examples include addition, subtraction, multiplication, and division problems.")
mathType = input()
if mathType == "1":
    print("You are doing arithmetic.")
    first = input("What is the first number in your problem?")
    second = input("What is the second number in your problem?")
    operation = input("What are we doing with this? 1 for Addition")
    arithmetic(first, second, operation)
else:
    print("I'm not yet programmed for this type of math.")

print(arithmetic)

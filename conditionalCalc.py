# A calculator that demonstrates conditional logic and simple functions

request = input("What type of operation would you like to do +, -, / or * ?")
Num1 = float(input("Please enter your first number:"))
Num2 = float(input("Please enter your second number:"))

plus = False
minus = False
divide = False
multiply = False
operator = False


def Add(Num1, Num2):
    sum = Num1 + Num2
    return sum


def Sub(Num1, Num2):
    sum = Num1 - Num2
    return sum


def Divide(Num1, Num2):
    sum = Num1 / Num2
    return sum


def Multiply(Num1, Num2):
    sum = Num1 * Num2
    return sum


if request == "+":
    plus = True
    answer = Add(Num1, Num2)
    print(Num1, "+", Num2, "is equal to ", answer)
if request == "-":
    answer = Sub(Num1, Num2)
    minus = True
    print(Num1, "-", Num2, "is equal to ", answer)
if request == "/":
    answer = Divide(Num1, Num2)
    divide = True
    print(Num1, "/", Num2, "is equal to ", answer)
if request == "*":
    answer = Multiply(Num1, Num2)
    print(Num1, "*", Num2, "is equal to ", answer)
    multiply = True
if plus or minus or divide or multiply:
    operator = True
    print("\n...Calculation complete...")
else:
    operator = False

a = int(input("Enter a number: "))
b = int(input("Enter Second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not mean to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")
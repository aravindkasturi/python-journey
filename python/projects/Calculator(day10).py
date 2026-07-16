print("""
 _____________________
|  _________________  |
| |                 | |
| |      0.000      | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | 0 | . | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

def cal(a):
    def operation(b):
        def next(c):
            if b == "+":
                return a + c
            elif b == "-":
                return a - c
            elif b == "*":
                return a * c
            elif b == "/":
                return a / c
            else:
                print("invalid")
                return a

        c = float(input("What's the next number?: "))
        result = next(c)
        print(f"{a} {b} {c} = {result}")
        return result

    return operation(input("+\n-\n*\n/\nPick an operation?: "))

a = float(input("What's the first number?: "))

con = True
while con:
    a = cal(a)

    choice = input(
        "Type 'y' to continue calculating with current result, "
        "or type 'n' to stop: "
    ).lower()

    if choice != "y":
        con = False
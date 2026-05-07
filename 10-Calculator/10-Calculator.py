import art

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {

    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("Enter first number: "))



    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Select an operator: ")
        num2 = float(input("Enter second number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Do you want to continue with {answer} or start a new calculation? (y/n): ").lower()
        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 40)
            calculator()


calculator()











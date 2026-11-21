def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        else:
            raise ValueError(f"Unsupported operator '{op}'. Use +, -, *, or /.")

        print(f"Result: {result}")
    except ValueError as e:
        print(f"ValueError: Invalid numeric input or operation. Details: {e}")
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")
    except Exception as e:
        print(f"Unexpected Error: {type(e).__name__} - {e}")


calculator()
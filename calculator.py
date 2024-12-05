while True:  

        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation ( +, -, /, ** or * ): ").strip()

        if operation.lower() == "exit":
            print("Exit")
            break
        
        num2 = float(input("Enter the second number: "))
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            if num2 == 0:  
                print("Is not possible.")
                continue
            result = num1 / num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "**":
            result = num1 ** num2
        else:
            print("Error: Please choose from ( +, -, /, *, or **)")
            continue
        print(f"The result of {num1} {operation} {num2} is: {result}\n")
       
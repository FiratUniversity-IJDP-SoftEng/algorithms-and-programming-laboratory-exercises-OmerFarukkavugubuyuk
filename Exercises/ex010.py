# Your Student ID:230543015
# Your Name and Surname:Ömer Faruk Kavuğubüyük
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Select an operation: +, -, *, /")
        operation = input("Operation: ")
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                continue
            result = num1 / num2
        else:
            print("Error: Invalid operation!")
            continue
        
        print(f"Result: {result}")
        
    except ValueError:
        print("Error: Please enter a valid number!")
    
    again = input("Do you want to perform another calculation? (Y/N): ").strip().lower()
    if again != "y":
        break

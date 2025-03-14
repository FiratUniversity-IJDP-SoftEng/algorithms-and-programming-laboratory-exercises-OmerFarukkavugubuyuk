# Your Student ID:230543015
# Your Name and Surname:Ömer Faruk Kavuğubüyük
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")

choice = input("Which conversion do you want to perform (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter Celsius value : "))
    print(f"Sonuç: {(celsius * 9/5) + 32:.2f} Fahrenheit")
elif choice == "2":
    fahrenheit = float(input("Enter Fahrenheit value: "))
    print(f"Sonuç: {(fahrenheit - 32) * 5/9:.2f} Celsius")
else:
    print("Please enter 1 or 2")

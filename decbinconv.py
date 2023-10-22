def decimal_to_binary(decimal):
    binary = bin(decimal).replace("0b", "")
    return binary

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

while True:
    print("Select an option:")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        decimal = int(input("Enter a decimal number: "))
        binary = decimal_to_binary(decimal)
        print(f"Binary representation: {binary}")
    elif choice == '2':
        binary = input("Enter a binary number: ")
        decimal = binary_to_decimal(binary)
        print(f"Decimal representation: {decimal}")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select a valid option.")
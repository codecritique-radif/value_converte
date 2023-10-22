import pint

# Create a unit registry
ureg = pint.UnitRegistry()

def convert_units(value, from_unit, to_unit):
    try:
        quantity = value * ureg(from_unit)
        converted_quantity = quantity.to(to_unit)
        return converted_quantity.magnitude, converted_quantity.units
    except pint.UndefinedUnitError as e:
        return f"Error: {e}"

while True:
    print("Select an option:")
    print("1. Perform Unit Conversion")
    print("2. Quit")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        value = float(input("Enter the value: "))
        from_unit = input("Enter the source unit (e.g., 'meters', 'feet', 'pounds', 'kilograms'): ")
        to_unit = input("Enter the target unit: ")
        converted_value, target_unit = convert_units(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {converted_value} {target_unit}")
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please select a valid option.")
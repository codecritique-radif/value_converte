from datetime import datetime
import pytz

# Define a dictionary of countries and their time zones
country_timezones = {
    "Bangladesh": "Asia/Dhaka",
    "South Africa": "Africa/Johannesburg",
    # Add more countries and their time zones here
}

def convert_time(input_time, from_country, to_country):
    try:
        from_tz = pytz.timezone(country_timezones[from_country])
        to_tz = pytz.timezone(country_timezones[to_country])
        from_time = from_tz.localize(input_time)
        to_time = from_time.astimezone(to_tz)
        return to_time
    except Exception as e:
        return f"Error: {e}"

while True:
    print("Select an option:")
    for i, country in enumerate(country_timezones.keys(), start=1):
        print(f"{i}. Convert Bangladesh Time to {country} Time")
    print(f"{len(country_timezones) + 1}. Quit")

    choice = input(f"Enter your choice (1/{len(country_timezones) + 1}): ")

    if choice == str(len(country_timezones) + 1):
        break
    elif choice.isnumeric() and 1 <= int(choice) <= len(country_timezones):
        from_country = "Bangladesh"
        to_country = list(country_timezones.keys())[int(choice) - 1]
        input_time_str = input("Enter time in Bangladesh (YYYY-MM-DD HH:MM): ")
        try:
            input_time = datetime.strptime(input_time_str, '%Y-%m-%d %H:%M')
            result_time = convert_time(input_time, from_country, to_country)
            print(f"Time in {to_country}: {result_time.strftime('%Y-%m-%d %H:%M')}")
        except ValueError:
            print("Invalid input time format.")
    else:
        print("Invalid choice. Please select a valid option.")
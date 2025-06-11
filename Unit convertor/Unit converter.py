def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

# Dictionary to store conversion options
conversion_options = {
    "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit, "°C", "°F"),
    "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius, "°F", "°C"),
    "3": ("Kilometers to Miles", km_to_miles, "km", "mi"),
    "4": ("Miles to Kilometers", miles_to_km, "mi", "km"),
    "5": ("Kilograms to Pounds", kg_to_pounds, "kg", "lb"),
    "6": ("Pounds to Kilograms", pounds_to_kg, "lb", "kg"),
}

def main():
    while True:
        print("\nUnit Converter Menu:")
        for key, value in conversion_options.items():
            print(f"{key}. {value[0]}")
        print("0. Exit")

        choice = input("Choose an option (0-6): ")

        if choice == "0":
            print("Exiting the converter. Goodbye!")
            break

        if choice not in conversion_options:
            print("Invalid choice. Try again.")
            continue

        try:
            value = float(input(f"Enter value in {conversion_options[choice][2]}: "))
        except ValueError:
            print("Invalid number entered. Try again.")
            continue

        # Perform conversion
        label, func, from_unit, to_unit = conversion_options[choice]
        result = func(value)
        print(f"{value:.2f} {from_unit} = {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()

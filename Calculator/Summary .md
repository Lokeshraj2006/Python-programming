# Unit Converter 

## Description

This is a menu-driven command-line unit converter built with Python. It allows users to convert values between different units of temperature, distance, and weight using clearly defined conversion formulas.

The program uses:
- Functions for each type of conversion
- A dictionary to store mappings and units
- Input validation and user-friendly prompts
- Clean formatted output with proper labels

---

## Features

- Convert:
  - Celsius ↔ Fahrenheit
  - Kilometers ↔ Miles
  - Kilograms ↔ Pounds
- Loop-based menu system
- Safe handling of invalid inputs
- Easy to read output format

---

## How It Works

### Functions Used

| Function Name               | Purpose                                  |
|----------------------------|------------------------------------------|
| `celsius_to_fahrenheit(c)` | Converts Celsius to Fahrenheit           |
| `fahrenheit_to_celsius(f)` | Converts Fahrenheit to Celsius           |
| `km_to_miles(km)`          | Converts Kilometers to Miles             |
| `miles_to_km(miles)`       | Converts Miles to Kilometers             |
| `kg_to_pounds(kg)`         | Converts Kilograms to Pounds             |
| `pounds_to_kg(pounds)`     | Converts Pounds to Kilograms             |

---

### Dictionary: `conversion_options`

A dictionary is used to:
- Map user input (`1`, `2`, `3`, etc.) to each conversion
- Store:
  - Description of the conversion
  - Function name
  - Input and output unit symbols (e.g., °C to °F)

**Output:**

![Unit convertor op](https://github.com/user-attachments/assets/0a6e3d0c-53c8-4c77-a973-2cdd19bddf18)

# Command-Line Calculator

## Description

This is a simple **command-line calculator** written in Python. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The program includes input validation and handles division by zero errors gracefully.

---

## Features

- Add, Subtract, Multiply, Divide
- Menu-driven interface using a loop
- Handles invalid input (e.g., non-numeric values)
- Prevents division by zero
- Clean formatted output

---

## Functions Used

| Function Name   | Purpose                          |
|----------------|----------------------------------|
| `add(x, y)`     | Returns the sum of `x` and `y`   |
| `subtract(x, y)`| Returns the difference `x - y`   |
| `multiply(x, y)`| Returns the product of `x` and `y`|
| `divide(x, y)`  | Returns the result of `x / y`; raises an error if `y = 0` |

---

## Main Program Flow

1. Displays a menu with operation options:
   - 1: Add
   - 2: Subtract
   - 3: Multiply
   - 4: Divide
   - 5: Exit
2. Takes user input for the desired operation.
3. Asks the user for two numbers.
4. Performs the chosen operation using the relevant function.
5. Displays the result in a formatted way, like:

**Output:**

![Calculator op](https://github.com/user-attachments/assets/050b042d-3ef1-46e2-9e99-a97e480897a2)


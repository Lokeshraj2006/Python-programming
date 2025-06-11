# Python Programming Internship - Codmetric


## Overview
This repository contains projects completed as part of the Python Programming Internship by CodMetric.
The internship was focused on applying core Python concepts through real-time mini-projects.
I developed five beginner-friendly command-line applications, each designed to build problem-solving skills and programming confidence.. These applications are:

1. Command-Line Calculator  
2. Unit Converter  
3. Number Guessing Game  
4. Rock, Paper, Scissors  
5. To-Do List Manager  

---

## 1. Command-Line Calculator
### Description
A basic calculator that performs addition, subtraction, multiplication, and division based on user input. The program runs in a loop until the user chooses to exit.

### Features
- Menu-driven interface
- Validates user input
- Handles division by zero

### Functions
- `add(x, y)`: Returns sum
- `subtract(x, y)`: Returns difference
- `multiply(x, y)`: Returns product
- `divide(x, y)`: Returns quotient or error for zero

---

## 2. Unit Converter
### Description
Converts units of temperature, distance, and weight. A dictionary stores conversion names, associated functions, and unit labels for flexible mapping.

### Features
- Separate functions for each conversion
- Menu-driven loop for user interaction
- Dictionary-based mapping of options
- Formatted output with unit labels

### Functions
- `celsius_to_fahrenheit(c)`
- `fahrenheit_to_celsius(f)`
- `km_to_miles(km)`
- `miles_to_km(miles)`
- `kg_to_pounds(kg)`
- `pounds_to_kg(pounds)`

---

## 3. Number Guessing Game
### Description
A game where the user guesses a randomly selected number between 1 and 100. The number of attempts is tracked, and appropriate feedback is given after each guess.

### Features
- Random number generation
- Tracks attempts taken
- Input validation
- Graceful exit via keyboard interrupt

### Functions
- `get_valid_guess()`: Validates user input
- `number_guessing_game()`: Game logic and loop

---

## 4. Rock, Paper, Scissors
### Description
A command-line version of the classic Rock, Paper, Scissors game where the user plays against the computer.

### Features
- Input validation for user choice
- Random computer choice
- Clearly defined winner logic
- Option to replay the game

### Functions
- `get_user_choice(choices)`: Validates input
- `determine_winner(user, computer)`: Determines the result
- `play_game()`: Game loop

---

## 5. To-Do List Manager
### Description
A simple command-line to-do list that lets users add, delete, and mark tasks as completed. Tasks are stored in a text file for persistence between sessions.

### Features
- Persistent task storage in `tasks.txt`
- Menu-driven task management
- Input validation and error handling

### Functions
- `load_tasks()`: Loads tasks from file
- `save_tasks(tasks)`: Saves tasks to file
- `display_tasks(tasks)`: Displays current tasks
- `add_task(tasks)`: Adds a new task
- `delete_task(tasks)`: Deletes a task by number
- `mark_completed(tasks)`: Marks a task as done

---

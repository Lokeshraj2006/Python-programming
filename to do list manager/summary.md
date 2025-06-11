# To-Do List Manager

## Overview
The To-Do List Manager is a simple Python command-line project that allows users to manage their daily tasks. It supports adding, deleting, and marking tasks as completed, with all tasks stored in a text file (`tasks.txt`) for persistence.

## Features
- Command-line interface for easy interaction
- Add, delete, and complete tasks
- Tasks are saved between sessions using a text file
- Input validation and error handling

## How It Works
The program maintains a list of tasks, where each task has:
- A description
- A completion status (`todo` or `done`)

Tasks are stored in `tasks.txt` in the format:
```
Task description | todo
Task description | done
```

Each time the program runs, it loads the tasks from the file and saves any changes made.

## Functions

### `load_tasks()`
Reads tasks from `tasks.txt`, parses each line, and returns a list of dictionaries representing tasks.

### `save_tasks(tasks)`
Writes the current task list to `tasks.txt`, preserving their completion status.

### `display_tasks(tasks)`
Displays all current tasks with numbering and status indicators.

### `add_task(tasks)`
Prompts the user to enter a new task description and adds it to the list.

### `delete_task(tasks)`
Prompts the user for the task number to delete and removes it from the list.

### `mark_completed(tasks)`
Marks a selected task as completed based on its number.

### `main()`
Main loop that shows the menu, handles user input, and invokes appropriate functions.

## Sample Menu
```
To-Do List Manager
1. Display tasks
2. Add task
3. Delete task
4. Mark task as completed
5. Exit
```
**Output**

![to do op 1](https://github.com/user-attachments/assets/48848968-2e12-4bee-a19b-cf2661c253f9)
![to do op2](https://github.com/user-attachments/assets/654b08d8-b240-40cb-b75c-e9db92bb919c)

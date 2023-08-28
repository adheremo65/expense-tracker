# Phase 3 CLI Project Template

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

YSure, here's a sample README file content for your Expense Tracker app:

---

# Expense Tracker App

The Expense Tracker App is a command-line interface (CLI) application that allows users to input their expenses and view a detailed table of their expenses, including a total of all expenses. This simple app is designed to help users keep track of their spending.

## Files

## ignore debug.py and seed.py files. They were only there to check validation at the begging stage of the development

### 1. `models.py`

The `models.py` module contains the SQLAlchemy model definitions for the `User` and `Expense` tables. It defines the structure of the database and the relationships between the tables. This module is responsible for handling interactions with the database and managing the user and expense data.

### 2. `user_input.py`

The `user_input.py` module handles user input and validation. It ensures that the user inputs are properly validated before processing. This module aims to provide a smooth and error-free user experience.

### 3. `cli.py`

This is the entry point of the application. It provides a menu-driven interface where users can perform actions such as logging in, viewing their total expenses per item in tabulr form and overall expense. The CLI interface is designed to be user-friendly and intuitive.

## Usage

1. Run the `cli.py` script to start the Expense Tracker App.
2. If you are a new user, you need to register by providing your username and password and input all your spending by running user_input.py script
3. Choose from the menu options:
   - **Log In:** Log in with your username and password.
   - **View Total Expense:** View a table displaying your expenses and the total sum of all expenses.
   - **Exit:** Quit the application.

## Installation

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Install the required packages using the following command:
   ```
   pip install -r requirements.txt
   ```

## Requirements

- Python 3.x
- SQLAlchemy
- Colorama
- Tabulate

## Contributions

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# ELEVATE-LABS-TASK-1-

Calculator CLI App
A simple command-line calculator application that supports basic arithmetic operations.
Features

✅ Addition (+)
✅ Subtraction (-)
✅ Multiplication (*)
✅ Division (/)
✅ Error handling for invalid inputs
✅ Division by zero protection
✅ User-friendly menu interface
✅ Continuous operation until user exits

Requirements

Python 3.6 or higher
VS Code (or any text editor)
Terminal/Command Prompt

Installation

Clone or download this repository to your local machine
Ensure Python is installed:

bash   python --version
If not installed, download from python.org
How to Run
Method 1: Using Terminal/Command Prompt

Navigate to the project directory:

bash   cd path/to/calculator-cli

Run the script:

bash   python calculator.py
Method 2: Using VS Code

Open the project folder in VS Code
Open calculator.py file
Press F5 or click Run > Start Debugging
Or right-click in the editor and select Run Python File in Terminal

Usage

When you run the program, you'll see a menu with operation choices
Enter a number (1-5) to select an operation:

1 for Addition
2 for Subtraction
3 for Multiplication
4 for Division
5 to Exit


Enter two numbers when prompted
View the result
Press Enter to continue or select option 5 to exit

Example
========================================
       CALCULATOR CLI APP
========================================
Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
========================================

Enter choice (1/2/3/4/5): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0

Press Enter to continue...
Project Structure
calculator-cli/
│
├── calculator.py      # Main calculator script
└── README.md         # Project documentation
Code Structure
The application uses a modular approach:

add(x, y) - Performs addition
subtract(x, y) - Performs subtraction
multiply(x, y) - Performs multiplication
divide(x, y) - Performs division with zero-check
display_menu() - Shows the operation menu
get_number(prompt) - Validates numeric input
main() - Main program loop


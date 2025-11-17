def add(x, y):
    """Addition operation"""
    return x + y

def subtract(x, y):
    """Subtraction operation"""
    return x - y

def multiply(x, y):
    """Multiplication operation"""
    return x * y

def divide(x, y):
    """Division operation"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("       CALCULATOR CLI APP")
    print("="*40)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("="*40)

def get_number(prompt):
    """Get valid number input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    """Main calculator function"""
    print("\nWelcome to Calculator CLI!")
    
    while True:
        display_menu()
        
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("\nThank you for using Calculator CLI. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        else:
            print("\nInvalid choice! Please select 1-5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
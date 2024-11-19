class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Create a Calculator object
calculator = Calculator(num1, num2)

# Calculate the sum
result = calculator.add()

# Print the result
print("The sum of", num1, "and", num2, "is:", result)
import sys

# Check if exactly two arguments are provided
if len(sys.argv) != 3:
    print("Error: Please provide exactly two numbers.")
    sys.exit()

# Convert arguments to float and add
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
print("Sum:", num1 + num2)

#completion of program
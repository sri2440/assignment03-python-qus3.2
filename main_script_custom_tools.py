# main_script_custom_tools.py
from custom_tools.calculator import add, subtract, multiply, divide
from custom_tools.file_handler import read_file, write_file, delete_file

# Calculator module usage
result_add = add(5, 3)
print(f"Addition: {result_add}")

result_subtract = subtract(10, 4)
print(f"Subtraction: {result_subtract}")

result_multiply = multiply(7, 2)
print(f"Multiplication: {result_multiply}")

try:
    result_divide = divide(9, 3)
    print(f"Division: {result_divide}")
except ValueError as e:
    print(f"Error: {e}")

# File handler module usage
file_path = 'example.txt'
file_content = 'Hello, custom_tools package!'

write_file(file_path, file_content)

read_content = read_file(file_path)
print(f"File Content:\n{read_content}")

delete_file(file_path)

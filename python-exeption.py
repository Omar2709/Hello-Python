def divide_by(a, b):
    try:
        result = a / b
    except Exception as e:
        return "Something went wrong: " + str(e)
    else:
        return result

print(divide_by(10, 2))  # Output: 5.0
print(divide_by(10, 0))  # Output: Something went wrong: division by zero
print(divide_by(10, "a"))  # Output: Something went wrong: unsupported operand type(s) for /: 'int' and 'str'

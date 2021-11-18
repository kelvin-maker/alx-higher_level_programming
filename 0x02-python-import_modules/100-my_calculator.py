#!/usr/bin/python3

from sys import argv, exit as sys_exit

from calculator_1 import add, sub, mul, div


if __name__ == "__main__":

ops = {"+": add, "-": sub, "*": mul, "/": div}
try:
a, op, b = argv[1:]

except ValueError:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys_exit(1)

    try:
        print(a, op, b, "=", ops[op](int(a), int(b)))

except KeyError:
    print("Unknown operator. Available operators: +, -, * and /")
    sys_exit(1)

except ValueError:
    print("Invalid operand. Must be an integer")
    sys_exit(1)

except ZeroDivisionError:
    print("Invalid operation. Cannot divide by zero")
    sys_exit(1)
                                                        

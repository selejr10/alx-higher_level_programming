#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    j = sys.argv

    if len(j) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if j[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(j[1])
    b = int(j[3])
    print("{} {} {} = {}".format(a, j[2], b, operators[j[2]](a, b)))

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    len_ = len(sys.argv)
    if len_ != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    operators = ['+', '-', '*', '/']
    operation = [cal.add, cal.sub, cal.mul, cal.div]
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, *, /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    k = 0
    for j in operators:
        if j == sys.argv[2]:
            print("{} {} {} = {}".format(a, j, b, operation[k](a, b)))
            break
        k += 1

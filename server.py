# script.py
# import pydevd; pydevd.settrace('localhost', port=5678)
import pdb; pdb.set_trace()
def add(x, y):
    result = x + y
    return result
import pdb; pdb.set_trace()
def subtract(x, y):
    result = x - y
    return result
import pdb; pdb.set_trace()
def multiply(x, y):
    result = x * y
    return result

def divide(x, y):
    result = x / y
    return result
import pdb; pdb.set_trace()
def main():
    a = 10
    b = 5
    sum_result = add(a, b)
    print(f"Sum: {sum_result}")

    sub_result = subtract(a, b)
    print(f"Difference: {sub_result}")

    mul_result = multiply(a, b)
    print(f"Product: {mul_result}")

    div_result = divide(a, b)
    print(f"Quotient: {div_result}")

if __name__ == "__main__":
    main()

"""FibonacciRecursionV1"""
def main(num):
    """FibonacciRecursionV1"""
    if num <= 1:
        return num
    return main(num-1)+main(num-2)
print(main(int(input())))

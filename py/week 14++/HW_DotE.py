"""HW_DotE"""
import math
def main(num):
    """"HW_DotE"""
    print(math.factorial(num)//(math.factorial(num//2)**2) if num%2 == 0 else \
        math.factorial(num+1)//(math.factorial((num+1)//2)**2))
main(int(input()))

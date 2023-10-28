"""Ink"""
import math
def main(ink):
    """Ink"""
    for _ in range(int(ink[1])):
        data = input().split()
        dis = ((int(data[0]))**2+(int(data[1]))**2)
        result = math.ceil((dis*3.1416)/int(ink[0]))
        print(result)
main(input().split())

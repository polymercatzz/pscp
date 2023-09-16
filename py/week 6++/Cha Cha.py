"""[Recommend + Midterm 2021] Cha Cha Cha"""
import math
def main():
    """[Recommend + Midterm 2021] Cha Cha Cha"""
    time_ = int(input())
    hours = 0
    for _ in range(time_):
        hours += math.ceil(float(input()))
    print(hours*8720)

main()

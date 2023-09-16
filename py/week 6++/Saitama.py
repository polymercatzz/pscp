"""[Midterm 2021] ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def kkk(num_1, num_2):
    """keep more"""
    if num_1 > num_2:
        return num_1
    return num_2

def main():
    """[Midterm 2021] ฉันจะเป็น Saitama ให้ได้เลย"""
    push = int(input())
    sit = int(input())
    squ = int(input())
    run = int(input())
    push_d = push/int(input())
    sit_d = sit/int(input())
    run_d = run/int(input())
    squ_d = squ/int(input())
    more = kkk(push_d, 0)
    more = kkk(more, sit_d)
    more = kkk(more, run_d)
    more = kkk(more, squ_d)
    print(math.ceil(more))
main()

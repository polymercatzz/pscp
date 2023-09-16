"""Circular I"""
def main():
    "Circular I"
    num_x1 = float(input())
    num_y1 = float(input())
    num_r = float(input())
    num_x2 = float(input())
    num_y2 = float(input())
    dis = ((num_x1-num_x2)**2+(num_y1-num_y2)**2)**0.5
    if dis > num_r:
        print("No")
    else:
        print("Yes")
main()

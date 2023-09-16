"""Circular II"""
def main():
    "Circular II"
    num_x1 = float(input())
    num_y1 = float(input())
    num_r1 = float(input())
    num_x2 = float(input())
    num_y2 = float(input())
    num_r2 = float(input())
    dis = ((num_x1-num_x2)**2+(num_y1-num_y2)**2)**0.5
    if dis >= num_r1+num_r2:
        print("No")
    else:
        print("Yes")
main()

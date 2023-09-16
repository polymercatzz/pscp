"""longer"""
import math
def main():
    """longer"""
    num_r = float(input())
    num_a = float(input())
    num_b = float(input())
    cir = 2*math.pi*num_r
    rec = 2*(num_a+num_b)
    if cir > rec:
        print("Circle is longer")
        print("%.5f"%(cir-rec))
    elif cir < rec:
        print("Rectangle is longer")
        print("%.5f"%(rec-cir))
    else:
        print("Equal")
        print("%.5f"%(rec-cir))

main()

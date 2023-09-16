"""Heron of Alexandria"""
def main():
    """Heron of Alexandria"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_s = (num_a+num_b+num_c)/2
    area = (num_s*(num_s-num_a)*(num_s-num_b)*(num_s-num_c))**0.5
    print("%.3f"%area)
main()

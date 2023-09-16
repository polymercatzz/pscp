"""Hamburger"""
def main():
    """Hamburger"""
    num_l = int(input())
    num_r = int(input())
    print(num_l*"|", 2*(num_l+num_r)*"*", num_r*"|", sep="")
main()

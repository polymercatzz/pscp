"""[Midterm 2020] Diamond"""
def main():
    """[Midterm 2020] Diamond"""
    num = int(input())
    mid = num//2
    for i in range(num):
        for j in range(num):
            if j+i == mid or abs(i-j) == mid or i+j == num+mid-1 or i == mid:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()

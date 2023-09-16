"""Right Arrow"""
def main():
    """Right Arrow"""
    num_n = int(input())
    num_k = int(input())
    for i in range(-num_k//2+1, num_k//2+1):
        print(" "*abs(num_k//2-abs(i))+"*"*num_n)
main()

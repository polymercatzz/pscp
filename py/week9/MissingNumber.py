"""MissingNumber"""
def main(num):
    """MissingNumber"""
    num_list = []
    for i in range(1, num+1):
        num_list.append(i)
    while True:
        num_in = int(input())
        if num_in == 0:
            break
        num_list.remove(num_in)
    print(*num_list, sep="\n")
main(int(input()))

"""Sort"""
def main():
    """Sort"""
    all_num = []
    while True:
        num = input()
        if num == "END":
            break
        all_num.append(int(num))
    for i in range(len(all_num), 0, -1):
        for j in range(i-1):
            if all_num[j] > all_num[j+1]:
                all_num[j+1], all_num[j] = all_num[j], all_num[j+1]
    print(*all_num, sep="\n")
main()

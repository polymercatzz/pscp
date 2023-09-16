"""[Recommend] Harshad Number"""
def main():
    """[Recommend] Harshad Number"""
    for _ in range(10):
        num = abs(int(input()))
        result = 0
        for i in str(num):
            result += int(i)
        if result == 0:
            print("No")
        elif int(num)%int(result) == 0:
            print("Yes")
        else:
            print('No')
main()

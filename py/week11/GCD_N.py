"""GCD_N"""
def main(num):
    """GCD_N"""
    result = 0
    lisr_num = [int(input()) for _ in range(num)]
    for i in range(len(lisr_num)-1):
        if i == 0:
            num1 = lisr_num[i]
        num2 = lisr_num[i+1]
        while num2 != 0:
            num1, num2 = num2, num1%num2
        result = num1
    print(result if num != 1  else lisr_num[0])
main(int(input()))

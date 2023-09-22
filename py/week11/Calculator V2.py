"""Calculator V2"""
def main(num):
    """Calculator V2"""
    ans = 0
    for i in range(len(str(num)), 0, -1):
        if i > 1:
            max_9 = int("9"+"0"*(i-1))
            minus_9 = int("9"*(i-1))
            ans += min(max_9, num-minus_9)*(i+1)
        else:
            ans += min(9, num)*(i+1)
    if ans == 2:
        ans //= 2
    print(ans)
main(int(input()))

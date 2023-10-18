"""SqFree"""
def main(num):
    """SqFree"""
    result = 0
    for j in range(1, num+1):
        check = 0
        for i in range(2, int(j**0.5)+1):
            if j%i**2 == 0:
                check = 1
                break
        if check == 0:
            result += 1
    print(result)
main(int(input()))

"SumOfNumber"
def main():
    "SumOfNumber"
    result = 0
    want_re = int(input())
    while True:
        num = int(input())
        if num == -1:
            break
        else:
            result += num
            if result == want_re:
                break
    print(result)

main()

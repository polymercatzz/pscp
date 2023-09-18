"""Binary"""
def main():
    """Binary"""
    num = int(input())
    result = ""
    while num > 0:
        result += str(num%2)
        num = num//2
    if result == "":
        print(0)
    else:
        print(result[::-1])
main()

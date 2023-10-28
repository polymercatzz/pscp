"""ISBN"""
def main(data):
    """ISBN"""
    result = 0
    muti = 10
    for i in data[:-1]:
        for j in i:
            result -= int(j)*muti
            muti -= 1
    result %= 11
    if result == 10:
        result = "X"
    if str(result) == data[-1]:
        print("Yes")
    else:
        print('No', result)
main(input().split("-"))

"""IP Address"""
def main(data):
    """IP Address"""
    data2 = data.copy()
    for i in data2:
        if not i.isnumeric():
            data.remove(i)
        elif int(i) > 255 or int(i) < 0:
            data.remove(i)
    if len(data2) == 4 and len(data) == 4:
        print(*list(map(int, data2)), sep=".")
    else:
        print("Invalid IPv4 address")
main(input().split("."))

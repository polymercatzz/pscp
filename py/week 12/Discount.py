"""Discount"""
def main():
    """Discount"""
    book = []
    while True:
        buy = input()
        if buy == "ENTER":
            book.sort()
            break
        book.append(int(buy))
    price = {0:0, 1:1, 2:2}
    dis = price.get(len(book)//6, len(book)//5)
    if dis == 3:
        dis = 2
    print(sum(book[dis:]))
main()

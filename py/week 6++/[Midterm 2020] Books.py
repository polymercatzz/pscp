"""[Midterm 2020] Books"""
import math
def main(book, page_per_b, numx, numy):
    """[Midterm 2020] Books"""
    day = 0
    read = (numx+day)/(numy+day)
    yester = 0
    today = 0
    page = page_per_b*book
    while page > 0:
        today = math.ceil(read*page_per_b)
        if today == page_per_b:
            day += math.ceil(page/page_per_b)
            break
        elif today + yester >= page_per_b:
            today = page_per_b-yester
            yester = 0
        else:
            yester += today
        page -= today
        day += 1
        read = (numx+day)/(numy+day)
    print(day)
main(int(input()), int(input()), int(input()), int(input()))

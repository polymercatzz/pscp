"""[Midterm 2020] Books"""
import math
def main(book, page_per_b, numx, numy):
    """[Midterm 2020] Books"""
    day = 0
    read = (numx+day)/(numy+day)
    for _ in range(book):
        page = 0
        while page < page_per_b:
            page += math.ceil(read*page_per_b)
            day += 1
            read = (numx+day)/(numy+day)
    print(day)
main(int(input()), int(input()), int(input()), int(input()))

"""Century"""
import math
def main():
    """Century"""
    time = int(input())
    for _ in range(time):
        whet_year = 0
        word = ""
        year = input()
        if "B.E." in year:
            whet_year -= 543
        for i in year:
            if i.isnumeric():
                word += i
        whet_year = math.ceil((whet_year+int(word))/100)
        if whet_year <= 0:
            print("ERROR")
        else:
            print(whet_year)
main()

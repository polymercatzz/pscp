"""[Midterm 2021] Saint Seiya"""
def main(time, punch):
    """[Midterm 2021] Saint Seiya"""
    result = 0
    for i in range(2, time+1, 2):
        if result >= punch:
            result += (12*(time-i+1))
            break
        elif i % 6 == 0:
            result += 1
        elif i % 2 == 0:
            result += 165
    print(result)
main(int(input()), int(input()))

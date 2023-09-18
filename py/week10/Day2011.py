"""Day2011"""
def main():
    """Day2011"""
    day_on = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = int(input())
    month = int(input())
    result = day_on[(sum(year[:month-1])+day)%7-1]
    print(result)
main()

"""[Midterm 2020 + Recommend] BTSMRT"""
def main():
    """[Midterm 2020 + Recommend] BTSMRT"""
    day = input()
    age = float(input())
    tall = float(input())
    if (day == "Children Day" and age < 14 and tall <= 140) or \
        (age < 14 and tall < 90):
        print("FREE")
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    else:
        print("PAY")

main()

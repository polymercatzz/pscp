"""Bonus"""
def main():
    """Bonus"""
    money = int(input())
    year = int(input())
    month = int(input())
    if month >= 10:
        year += 1
    if year > 20:
        year = 20
    bonus = min(1000000, max(5000, year*money))
    print(bonus)

main()

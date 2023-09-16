"""ProgressiveTax"""
def main():
    """ProgressiveTax"""
    salary = int(input())
    tax = 0
    if salary > 4000000:
        tax += int((salary-4000000)*0.35)
        salary = 4000000
    if salary > 2000000:
        tax += int((salary-2000000)*0.30)
        salary = 2000000
    if salary > 1000000:
        tax += int((salary-1000000)*0.25)
        salary = 1000000
    if salary > 750000:
        tax += int((salary-750000)*0.20)
        salary = 750000
    if salary > 500000:
        tax += int((salary-500000)*0.15)
        salary = 500000
    if salary > 300000:
        tax += int((salary-300000)*0.10)
        salary = 300000
    if salary > 150000:
        tax += int((salary-150000)*0.05)
        salary = 150000
    print(tax)
main()

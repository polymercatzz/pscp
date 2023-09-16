"BMI"
def bmi():
    "cal bmi"
    weight = float(input())
    tall = float(input())
    bmi_ = weight/(tall/100)**2
    return bmi_
def main():
    "main"
    name_1 = input()
    bmi_1 = bmi()
    name_2 = input()
    bmi_2 = bmi()
    name_3 = input()
    bmi_3 = bmi()
    name_4 = input()
    bmi_4 = bmi()
    name_5 = input()
    bmi_5 = bmi()
    print("%s's  BMI = %.2f"%(name_1, bmi_1))
    print("%s's  BMI = %.2f"%(name_2, bmi_2))
    print("%s's  BMI = %.2f"%(name_3, bmi_3))
    print("%s's  BMI = %.2f"%(name_4, bmi_4))
    print("%s's  BMI = %.2f"%(name_5, bmi_5))
main()

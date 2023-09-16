'''planCDE'''
def main():
    '''input'''
    data = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if data == "Ascend":
        asc(num1, num2, num3)
    elif data == "Descend":
        desc(num1, num2, num3)

def asc(num1, num2, num3):
    '''ascend'''
    if num1 <= num2 <= num3:
        print("%.2f"%num1+",", "%.2f"%num2+",", "%.2f"%num3)
    elif num1 <= num3 <= num2:
        print("%.2f"%num1+",", "%.2f"%num3+",", "%.2f"%num2)
    elif num2 <= num1 <= num3:
        print("%.2f"%num2+",", "%.2f"%num1+",", "%.2f"%num3)
    elif num2 <= num3 <= num1:
        print("%.2f"%num2+",", "%.2f"%num3+",", "%.2f"%num1)
    elif num3 <= num2 <= num1:
        print("%.2f"%num3+",", "%.2f"%num2+",", "%.2f"%num1)
    else:
        print("%.2f"%num3+",", "%.2f"%num1+",", "%.2f"%num2)
def desc(num1, num2, num3):
    '''descend'''
    if num1 >= num2 >= num3:
        print("%.2f"%num1+",", "%.2f"%num2+",", "%.2f"%num3)
    elif num1 >= num3 >= num2:
        print("%.2f"%num1+",", "%.2f"%num3+",", "%.2f"%num2)
    elif num2 >= num1 >= num3:
        print("%.2f"%num2+",", "%.2f"%num1+",", "%.2f"%num3)
    elif num2 >= num3 >= num1:
        print("%.2f"%num2+",", "%.2f"%num3+",", "%.2f"%num1)
    elif num3 >= num2 >= num1:
        print("%.2f"%num3+",", "%.2f"%num2+",", "%.2f"%num1)
    else:
        print("%.2f"%num3+",", "%.2f"%num1+",", "%.2f"%num2)
main()

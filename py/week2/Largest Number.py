"Largest Number"
def num_more(num_1, num_2, num_3):
    "num more"
    if int(num_1) < int(num_2):
        num_1, num_2 = num_2, num_1
    if int(num_2) < int(num_3):
        num_2, num_3 = num_3, num_2
    if int(num_1) < int(num_2):
        num_1, num_2 = num_2, num_1
    result = int(str(num_1)+str(num_2)+str(num_3))
    return result
def main():
    "Largest Number"
    num_1 = input()
    num_2 = input()
    num_3 = input()
    result = num_more(num_1, num_2, num_3)
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    if num_2 < num_3:
        num_2, num_3 = num_3, num_2
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    if len(num_1) > len(num_2):
        num_1, num_2 = num_2, num_1
    if len(num_2) > len(num_3):
        num_2, num_3 = num_3, num_2
    if len(num_1) > len(num_2):
        num_1, num_2 = num_2, num_1
    if num_1[0] < num_2[0]:
        num_1, num_2 = num_2, num_1
    if num_2[0] < num_3[0]:
        num_2, num_3 = num_3, num_2
    if num_1[0] < num_2[0]:
        num_1, num_2 = num_2, num_1
    result_2 = int(num_1+num_2+num_3)
    if result_2 > result:
        print(result_2)
    else:
        print(result)
main()

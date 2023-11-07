# """[Recommended] Poisonous Vegetables"""
# def main(size, area, day):
#     """[Recommended] Poisonous Vegetables"""
#     result = [input().replace("[", "")[:-1].split("]") for _ in range(int(size[0]))]
#     for i in result:
#         for j in i:
#             j = list(map(int, j.split(" ")))
#             if j[1] > area:
#                 print("[ - ]", end="")
#             elif j[0] == j[-1] and j[0] <= day:
#                 print("[ o ]", end="")
#             else:
#                 print("[ x ]", end="")
#         print()
# main(input(), int(input()), int(input()))
'''[Recommended] Coupon'''
def main():
    '''[Recommended] Coupon'''
    price = float(input())
    pro1 = input().split()
    pro2 = input().split()
    if price >= float(pro1[1]):
        sel = price - float(pro1[0])
    if price >= float(pro2[1]):
        sel2 = (price*(100-float(pro2[0])))/100
    if price < float(pro1[1]) or price < float(pro2[1]):
        print("Nope")
    else:
        if sel == sel2:
            if min(float(pro1[1]), float(pro2[1])) == float(pro1[1]):
                print("1 %.1f"%sel)
            elif min(float(pro1[1]), float(pro2[1])) == float(pro2[1]):
                print("2 %.1f"%sel)
        elif sel < sel2 or (sel == sel2 and pro1[1] == pro2[1]):
            print("1 %.1f"%sel)
        else:
            print("2 %.1f"%sel2)
main()
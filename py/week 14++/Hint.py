"""Hint"""
def main(lst, mid, fnt):
    """Hint"""
    d_lst = {"=":{int(lst[-1])}, ">":set(range(int(lst[-1])+1, 10)), \
            "<":set(range(0, int(lst[-1]))), "!":set(range(10))-{int(lst[-1])}}
    d_mid = {"=":{int(mid[-1])}, ">":set(range(int(mid[-1])+1, 10)), \
            "<":set(range(0, int(mid[-1]))), "!":set(range(10))-{int(mid[-1])}}
    d_fnt = {"=":{int(fnt[-1])}, ">":set(range(int(fnt[-1])+1, 10)), \
            "<":set(range(0, int(fnt[-1]))), "!":set(range(10))-{int(fnt[-1])}}
    lst = d_lst.get(lst[0]) if lst[1] != "=" or lst[0] == "!" else d_lst.get(lst[0])|{int(lst[-1])}
    mid = d_mid.get(mid[0]) if mid[1] != "=" or mid[0] == "!"else d_mid.get(mid[0])|{int(mid[-1])}
    fnt = d_fnt.get(fnt[0]) if fnt[1] != "=" or fnt[0] == "!"else d_fnt.get(fnt[0])|{int(fnt[-1])}
    for i in sorted(fnt):
        for j in sorted(mid):
            for k in sorted(lst):
                print("%d%d%d"%(i, j, k))
main(input(), input(), input())

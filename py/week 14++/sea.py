"""เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
def main(animal):
    """เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
    ans = []
    data = {"BULL SHARK":"THE SHALLOW ZONE", \
        "CHAIN CATSHARK,GREAT WHITE SHARK,GUMMY SHARK,BLUE SHARK,MAKO SHARK":\
        "THE TWILIGHT ZONE", \
        "FRILLED SHARK,GOBLIN SHARK,SIXGILL SHARK,GREENLAND SHARK,COOKIECUTTER SHARK,":\
        "THE MIDNIGHT ZONE", "MEGAMOUTH SHARK":"THE ABYSSAL ZONE"}
    for i, j in data.items():
        if animal in i and "SHARK" in animal:
            ans.append(j)
    print(ans[0] if ans else "ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
main(input())

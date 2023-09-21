"""Cat Parade"""
def main():
    """Cat Parade"""
    list_cat = []
    name = []
    result = []
    order = 1
    while True:
        word = input()
        if word == "END":
            break
        elif word == "IT'S A DOG":
            list_cat.remove(list_cat[-1])
        else:
            list_cat += word.split(", ")
    for i in list_cat:
        if not i in name:
            name.append(i)
            result.append(i+" "+str(order)+" "+str(list_cat.count(i)))
        order += 1
    result.sort()
    print(*result, sep="\n")
main()

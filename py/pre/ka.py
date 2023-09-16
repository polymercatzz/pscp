'''kayak'''
def main():
    '''kayak'''
    kayak_list = []
    new_list = []
    kon = int(input())
    weight = input()
    if kon != 0:
        weight_list = weight.split(" ")
        for i in range(len(weight_list)):
            weight_list[i] = int(weight_list[i])
        weight_list.sort(reverse=True)
        for i in weight_list:
            if i not in new_list:
                new_list.append(i)
            else:
                new_list.remove(i)
                kayak_list.append(0)
                kon -= 1
        for _ in range(kon):
            kayak_list.append(new_list[0]-new_list[1])
            del new_list[:2]
        kayak_list.sort(reverse=True)
        del kayak_list[0]
        print(sum(kayak_list))
    else:
        print(sum(kayak_list))
main()

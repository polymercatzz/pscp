"kayak"
def main():
    '''kayak'''
    new_list = []
    result_1 = 0
    result_2 = 0
    kon = int(input())
    weight = input()
    weight_list = weight.split(" ")
    if kon > 0:
        for i in range(len(weight_list)):
            weight_list[i] = int(weight_list[i])
        for i in weight_list:
            if i not in new_list:
                new_list.append(i)
            else:
                new_list.remove(i)
                kon -= 1
        new_list = sorted(new_list)
        for i in new_list:
            new_list_2 = new_list.copy()
            new_list_2.remove(i)
            for j in new_list_2:
                sum_lst = []
                time_ = 0
                new_list_3 = new_list_2.copy()
                new_list_3.remove(j)
                for kon in range(len(new_list_3)//2):
                    result_1 = new_list_3[time_+1]-new_list_3[time_]
                    time_ += 2
                    sum_lst.append(int(result_1))
                result_1 = sum(sum_lst)
                if result_1 > 0 and result_2 == 0:
                    result_2 = result_1
                elif result_1 < result_2 and result_1 > 0:
                    result_2 = result_1
    print(result_2)
main()

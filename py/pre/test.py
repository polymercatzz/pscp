'''kayak'''
def pri(kayak, kayak_1):
    "pri"
    if sum(kayak) < sum(kayak_1):
        result = (sum(kayak))
    elif sum(kayak) > sum(kayak_1):
        result = (sum(kayak_1))
    else:
        result = (sum(kayak))
    return result
def main():
    '''kayak'''
    kayak = [0]
    kayak_1 = [0]
    new_list = []
    result = 0
    result_2 = 0
    list_time = 0
    time_ = 0
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
        new_list_1 = sorted(new_list)
        new_list_2 = sorted(new_list)
        for _ in range(kon):
            result = new_list_1[time_+1]-new_list_1[time_]
            if result > result_2:
                result_2 = result
                list_time = time_
            time_ += 2
        if kon > 0:
            del new_list_1[list_time]
            del new_list_1[list_time]
        time_ = 0
        for _ in range(kon-1):
            result = new_list_1[time_+1]-new_list_1[time_]
            kayak.append(result)
        if kon > 0:
            del new_list_2[0]
            del new_list_2[-1]
        time_ = 0
        for _ in range(kon-1):
            result = new_list_2[time_+1]-new_list_2[time_]
            kayak_1.append(result)
    result = pri(kayak, kayak_1)
    print(result)
main()

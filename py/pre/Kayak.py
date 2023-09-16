"Kayak"
def main():
    'main'
    num = int(input())
    weight = input()
    weight_list = []
    nweight_list = []
    num_ = 0
    duo = 0
    result_ = 0
    result = 0
    weight_list = weight.split()
    if num > 0:
        for weight in weight_list:
            weight = weight.replace("'", "")
            weight = int(weight)
            if weight not in nweight_list:
                nweight_list.append(weight)
            else:
                nweight_list.remove(weight)
                duo += 1
        nweight_list = sorted(nweight_list)
        num = int(num-1-duo)
        for num in range(num):
            result = nweight_list[num_+1]-nweight_list[num_]
    print(result)
main()

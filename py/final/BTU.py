"""BTU"""
def main(size, high, people, type1, type2):
    """BTU"""
    result = 0
    dict_size = {150:5000, 250:6000, 300:7000, 350:8000, 400:9000, 450:10000, 550:12000, \
                700:14000, 1000:18000, 1200:21000, 1400:23000, 1500:24000, 2000:30000, 2500:34000}
    for key, value in dict_size.items():
        if size <= key:
            result += value
            break
    if high > 8:
        result += (high-8)*1000
    if people > 2:
        result += (people-2)*600
    if type1 == "kitchen":
        result += 4000
    if type2 == "facing the sun":
        result = result*1.1
    elif type2 == "shaded":
        result = result*0.9
    print(int(result))
main(int(input()), int(input()), int(input()), input(), input())

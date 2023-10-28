"""SceneSwitch I"""
def main():
    """SceneSwitch I"""
    color = True
    data = []
    result = 0
    while True:
        word = input()
        if word == "End":
            break
        data.append(float(word))
    for i in range(len(data)):
        if i%2 == 0 and color and i not in (0, 1):
            if data[i]-data[i-1] <= 6:
                color = False
                result += 1
        elif i%2 == 0 and i not in (0, 1) and not color:
            color = True
    print(result)
main()

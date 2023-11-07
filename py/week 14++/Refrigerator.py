"""Refrigerator"""
def main(num, food):
    """Refrigerator"""
    day = 0
    food = {i:int(food[i]) for i in range(num)}
    while min(food.values()) != 0:
        keep = min(food.items(), key=lambda x: x[1])
        for i in food:
            if i != keep[0]:
                food[i] -= 1
        day += 1
    print(day)
main(int(input()), input().split(" "))

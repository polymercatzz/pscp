"Brick Bridge"
def main():
    "Brick Bridge"
    rock_a = int(input())
    rock_b = int(input())
    goal = int(input())
    rock_b_want = goal//5
    b_use = min(rock_b_want, rock_b)
    a_use = goal-b_use*5
    if a_use <= rock_a:
        print(a_use)
    else:
        print(-1)
main()

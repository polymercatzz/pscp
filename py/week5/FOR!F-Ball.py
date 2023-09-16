"""FOR!F-Ball"""
def ball(word):
    """FOR!F-Ball"""
    ball_1 = 1
    ball_2 = 0
    ball_3 = 0
    for i in word:
        if i == "A":
            ball_1, ball_2 = ball_2, ball_1
        elif i == "B":
            ball_2, ball_3 = ball_3, ball_2
        else:
            ball_1, ball_3 = ball_3, ball_1
    if ball_1 == 1:
        print(1)
    elif ball_2 == 1:
        print(2)
    else:
        print(3)
ball(input())

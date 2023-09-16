"""Ball"""
def ball(num):
    """Ball"""
    jump = 0
    while num*0.6 > 0.01:
        jump += 1
        num = num*0.6
    print(jump)
ball(float(input()))

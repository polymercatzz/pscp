"""PongYa"""
def main(num):
    """PongYa"""
    if num%3 == 0 or str(num)[-1] == "3":
        print("PONG")
    else:
        print(num)
main(int(input()))

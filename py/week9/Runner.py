"""Runner"""
def main(meter, people):
    """Runner"""
    runner = {}
    for i in range(1, people+1):
        speed = tuple(input().split(" "))
        runner[i] = (meter-int(speed[1]))/int(speed[0]), -int(speed[0])
    result = min(runner, key=runner.get)
    print(result)
main(float(input()), int(input()))

"""Restaurant"""
def main():
    """Restaurant"""
    cost_food = float(input())
    promo = float(input())
    percen = float(input())
    food = float(input())
    buy_food = cost_food+food
    discout = buy_food
    if cost_food == promo:
        cost_food = cost_food*(1-(percen/100))
    if buy_food >= promo:
        discout = buy_food*(1-(percen/100))
    if discout < cost_food:
        print("Yes %.3f"%(abs(discout-cost_food)))
    elif discout > cost_food:
        print("No %.3f"%(abs(discout-cost_food)))
    else:
        print("Yes")

main()

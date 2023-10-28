"""Apartment"""
def main():
    """Apartment"""
    room_all = int(input())
    base_price = int(input())
    room_now = int(input())
    discount = int(input())
    new_price = [0, 0]
    result = [[base_price*room_now, room_now]]
    add = int(input())
    if room_now < room_all:
        room = min(room_all-room_now, base_price//discount)
        new_price = [(room+room_now)*(base_price-(room*discount)), room_now+room]
        result.append(new_price)
    elif room_now == room_all and room_all != 0:
        room = room_all
        for i in range(1, room):
            if (room_now-i)*(base_price+(i*add)) < new_price[0]:
                break
            new_price = [(room_now-i)*(base_price+(i*add)), room_now-i]
        result.append(new_price)
    result.sort(key=lambda x: (-x[0], x[1]))
    print(*result[0], sep="\n")
main()

"""BusStop I"""
def main(people, bus_sta):
    """BusStop I"""
    bus_stop = []
    bus = []
    count = 0
    for i in range(bus_sta):
        bus_stop.append(input().strip().split(" "))
    bus_stop.sort(key=lambda x: int(x[0]))
    for i in bus_stop:
        while i[0] in bus:
            count += 1
            bus.remove(i[0])
        for j in i[1:]:
            if int(j) > int(i[0]) and len(bus) < people:
                bus.append(j)
            if people == len(bus):
                break
    print(count)
main(int(input()), int(input()))

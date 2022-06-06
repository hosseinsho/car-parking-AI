
def h_func(node):
    ret = 0
    parking = node.map()
    car = node.cars[0]
    for col in range(car['col'] + car['l'], node.w):
        if parking[car['row']][col] == 1:
            ret += 1
    return ret

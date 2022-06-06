
class Node:
    def __init__(self, w, h, cars):
        self.w = w
        self.h = h
        self.cars = cars
        self._init_hash()

    def _do_move(self, idx, dis):
        new_cars = list(self.cars)
        car = new_cars[idx].copy()
        if car['o'] == HOR:
            car['col'] += dis
        elif car['o'] == VER:
            car['row'] += dis
        new_cars[idx] = car
        return Node(self.w, self.h, new_cars)

    def map(self):
        ret = [[0 for col in range(self.w)] for row in range(self.h)]
        for car in self.cars:
            for d in range(car['l']):
                if car['o'] == HOR:
                    ret[car['row']][car['col'] + d] = 1
                else:
                    ret[car['row'] + d][car['col']] = 1
        return ret

    def neighbors(self):
        ret = []
        parking = self.map()
        for idx in range(len(self.cars)):
            car = self.cars[idx]
            # forward
            if car['o'] == HOR:
                lim = self.w - (car['col'] + car['l'] - 1)
            else:
                lim = self.h - (car['row'] + car['l'] - 1)
            for d in range(1, lim):
                if car['o'] == HOR:
                    x = parking[car['row']][car['col'] + car['l'] - 1 + d]
                else:
                    x = parking[car['row'] + car['l'] - 1 + d][car['col']]
                if x == 1:
                    break
                ret.append(self._do_move(idx, d))
            # backward
            if car['o'] == HOR:
                lim = car['col'] + 1
            else:
                lim = car['row'] + 1
            for d in range(-1, -lim, -1):
                if car['o'] == HOR:
                    x = parking[car['row']][car['col'] + d]
                else:
                    x = parking[car['row'] + d][car['col']]
                if x == 1:
                    break
                ret.append(self._do_move(idx, d))
        return ret

    def _init_hash(self):
        h = 0
        for el in self.cars:
            h = (h * 701 + hash((el['row'], el['col'])))
        self._hash = h & 0xFFFFFFFF

    def __hash__(self):
        return self._hash

    def __lt__(self, other):
        return hash(self) < hash(other)

    def __eq__(self, other):
        return hash(self) == hash(other)

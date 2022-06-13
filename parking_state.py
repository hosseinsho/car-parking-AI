
HORIZONTAL = 'h'
VERTICAL = 'v'


class ParkingState:
    def __init__(self, x, y, cars):
        self.x = x
        self.y = y
        self.cars = cars
        self._init_hash()
        self.h_value = 0
        self.calculate_heuristic()
        self.g_value = 0
        self.f_value = self.g_value + self.h_value

    def calculate_heuristic(self):
        h_val = 0
        parking = self.get_state_map()
        red_car = self.cars[0]
        for col in range(red_car['col'] + red_car['length'], self.y):
            if parking[red_car['row']][col] == 1:
                h_val += 1
        self.h_value = h_val

    def set_g_value(self, g_value):
        self.g_value = g_value
        self.f_value = self.g_value + self.h_value

    def move_car_with_id(self, index, dist):
        new_cars = list(self.cars)
        car = new_cars[index].copy()
        if car['pos'] == HORIZONTAL:
            car['col'] += dist
        elif car['pos'] == VERTICAL:
            car['row'] += dist
        new_cars[index] = car
        return ParkingState(self.x, self.y, new_cars)

    def get_state_map(self):
        state_map = [[0 for _ in range(self.x)] for _ in range(self.y)]

        for car in self.cars:
            for d in range(car['length']):
                if car['pos'] == HORIZONTAL:
                    state_map[car['row']][car['col'] + d] = 1
                else:
                    state_map[car['row'] + d][car['col']] = 1

        return state_map

    def find_child_states(self):
        children = []
        parking_map = self.get_state_map()

        for index, car in enumerate(self.cars):
            # move car right/down
            if car['pos'] == HORIZONTAL:
                move_limit = self.x - (car['col'] + car['length'] - 1)
            else:
                move_limit = self.y - (car['row'] + car['length'] - 1)

            for d in range(1, move_limit):
                if car['pos'] == HORIZONTAL:
                    is_occupy = parking_map[car['row']][car['col'] + car['length'] - 1 + d]
                else:
                    is_occupy = parking_map[car['row'] + car['length'] - 1 + d][car['col']]
                if is_occupy:
                    break
                children.append(self.move_car_with_id(index, d))

            # move car left/up
            if car['pos'] == HORIZONTAL:
                move_limit = car['col'] + 1
            else:
                move_limit = car['row'] + 1

            for d in range(-1, -move_limit, -1):
                if car['pos'] == HORIZONTAL:
                    is_occupy = parking_map[car['row']][car['col'] + d]
                else:
                    is_occupy = parking_map[car['row'] + d][car['col']]
                if is_occupy:
                    break
                children.append(self.move_car_with_id(index, d))

        return children

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

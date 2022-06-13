from algorithms import a_star_algorithm
from parking_state import ParkingState


def main():
    num_parking = int(input())
    for parking in range(num_parking):
        x, y, car_num = list(map(int, input().split()))
        cars = []

        for _ in range(car_num):
            row, col, pos, length = list(input().split())
            row = int(row) - 1
            col = int(col) - 1
            cars.append({
                'col': col,
                'row': row,
                'pos': pos,
                'length': int(length)
            })

        start_state = ParkingState(x, y, cars)
        cost = a_star_algorithm(start_state)

        print("Test #", parking + 1, ": ", cost + 1, sep='')


if __name__ == '__main__':
    main()

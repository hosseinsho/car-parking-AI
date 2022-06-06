from algorithms import a_star_graph
from node import Node

INF = 127
HOR = 0
VER = 1


def main():
    T = int(input())
    for t in range(T):
        [N, M, V] = [int(x) for x in input().split()]
        cars = []
        for v in range(V):
            [row, col, o, l] = [x for x in input().split()]
            row = int(row) - 1
            col = int(col) - 1
            o = HOR if o == 'h' else VER
            l = int(l)
            cars.append({'col': col, 'row': row, 'o': o, 'l': l})
        root = Node(M, N, cars)
        cost = a_star_graph(root)
        print("Test #", t + 1, ": ", cost + 1, sep='')


if __name__ == '__main__':
    main()

from queue import PriorityQueue

INF = 127


def h_func(node):
    ret = 0
    parking = node.map()
    car = node.cars[0]
    for col in range(car['col'] + car['l'], node.w):
        if parking[car['row']][col] == 1:
            ret += 1
    return ret


def goal_test(node):
    return h_func(node) == 0


def a_star_graph(start):
    g = {start: 0}
    h = {start: h_func(start)}
    f = lambda node: g[node] + h[node]

    closed_set = set()
    open_set = PriorityQueue()
    open_set.put((f(start), start))

    while not open_set.empty():
        u = open_set.get()[1]
        if u in closed_set:
            continue
        if goal_test(u):
            return g[u]

        closed_set.add(u)
        neighbors = u.neighbors()
        for v in neighbors:
            if v in closed_set:
                continue
            if v not in g:
                h[v] = h_func(v)
                g[v] = INF
            new_g = g[u] + 1
            if new_g < g[v]:
                g[v] = new_g
                open_set.put((f(v), v))

    return -1

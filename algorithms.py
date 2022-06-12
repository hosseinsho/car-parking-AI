from queue import PriorityQueue
from parking_state import ParkingState

INF = 127


def calculate_heuristic_value(state: ParkingState):
    h_value = 0
    parking = state.get_state_map()
    red_car = state.cars[0]
    for col in range(red_car['col'] + red_car['length'], state.y):
        if parking[red_car['row']][col] == 1:
            h_value += 1
    return h_value


def a_star_graph(start_state: ParkingState):
    g_value = {start_state: 0}
    h_value = {start_state: calculate_heuristic_value(start_state)}
    f = lambda state: g_value[state] + h_value[state]

    closed_states = set()
    open_states = PriorityQueue()
    open_states.put((f(start_state), start_state))

    while not open_states.empty():
        state = open_states.get()[1]

        if state in closed_states:
            continue

        if calculate_heuristic_value(state) == 0:
            return g_value[state]

        closed_states.add(state)
        children = state.find_child_states()

        for child_state in children:
            if child_state in closed_states:
                continue

            if child_state not in g_value:
                h_value[child_state] = calculate_heuristic_value(child_state)
                g_value[child_state] = INF

            new_g = g_value[state] + 1

            if new_g < g_value[child_state]:
                g_value[child_state] = new_g
                open_states.put((f(child_state), child_state))

    return -1

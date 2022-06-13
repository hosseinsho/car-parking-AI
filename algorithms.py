from queue import PriorityQueue
from parking_state import ParkingState

MAX_G_VALUE = 150


def a_star_algorithm(start_state: ParkingState):
    closed_states = set()
    open_states = PriorityQueue()
    open_states.put((start_state.f_value, start_state))

    while not open_states.empty():
        state = open_states.get()[1]

        if state in closed_states:
            continue

        if state.h_value == 0:
            return state.g_value

        closed_states.add(state)
        children = state.find_child_states()

        for child_state in children:
            if child_state in closed_states:
                continue

            child_g_value = state.g_value + 1

            if child_g_value < MAX_G_VALUE:
                child_state.set_g_value(child_g_value)
                open_states.put((child_state.f_value, child_state))

    return -1

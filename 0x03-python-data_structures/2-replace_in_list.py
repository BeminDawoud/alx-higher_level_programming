#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for n_id, v in enumerate(my_list):
        if n_id == idx:
            my_list[n_id] = element
            return my_list

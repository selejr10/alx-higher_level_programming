#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0:
        return (copy)
    if idx >= len(my_list):
        return (copy)
    else:
        new = []
        new += my_list
        new[idx] = element
        return (new)

#!/usr/bin/python3
def add_tuple(tuple_a = (), tuple_b = ()):
    if tuple_a == () and tuple_b == ():
        return (0, 0)
    elif tuple_a == ():
        return tuple_b
    elif tuple_b == ():
        return tuple_a
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        return (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        return (tuple_a[0] + tuple_b[0], tuple_a[1])
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        return (tuple_a[0] + tuple_b[0], 0)
    else:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

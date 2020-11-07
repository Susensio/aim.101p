# Programming for the Puzzled -- Srini Devadas
# You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps
# Output is a set of commands (printed out) to get either all F's or all B's
# Fewest commands are the goal

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'F', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']


def print_func_name(f):
    def inner(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)
    return inner


@print_func_name
def pleaseConformOpt(caps):
    # Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    caps = caps + ['END']

    # Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))

            if caps[start] == 'F':
                forward += 1
            elif caps[start] == 'B':
                backward += 1
            else:
                pass
            start = i

    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            # Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]:
                print('Person at position', t[0], 'flip your cap!')
            else:
                print('People in positions',
                      t[0], 'through', t[1], 'flip your caps!')


@print_func_name
def pleaseConformOnepass(caps):
    if len(caps) == 0:
        print("Empty stadium!")
    else:
        start = 0
        caps = caps + [caps[0]]

        for i in range(1, len(caps)):
            if caps[i] != caps[i-1]:
                if caps[i] != caps[0]:
                    start = i
                else:
                    if start == i-1:
                        print('Person at position', start, 'flip your cap!')
                    else:
                        print('People in positions',
                              start, 'through', i-1, 'flip your caps!')


if __name__ == "__main__":
    # pleaseConformOpt(caps)
    # pleaseConformOnepass(caps)
    # pleaseConformOnepass([])
    pleaseConformOpt(cap3)

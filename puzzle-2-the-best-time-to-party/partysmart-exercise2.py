# Programming for the Puzzled -- Srini Devadas
# The Best Time to Party
# Given a list of intervals when celebrities will be at the party
# Output is the time that you want to go the party when the maximum number of
# celebrities are still there.
# Algorithm that choose the celebrity whose start time is cointained in the maximun
# number of other celebrity intervals

sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
         (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
sched3 = [(6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8),
          (9, 10), (11, 12), (11, 13), (11, 14)]


def bestTimeToPartyInterval(schedule):
    time = None
    maxcount = 0

    for i, (comes, goes) in enumerate(schedule):
        count = 0
        # Compare to the rest of the list
        for other_comes, other_goes in (schedule[:i] + schedule[i+1:]):
            if other_comes <= comes < other_goes:
                count += 1

        if count > maxcount:
            maxcount = count
            time = comes

    # Output best time to party
    print('Best time to attend the party is at', time,
          'o\'clock', ':', maxcount, 'celebrities will be attending!')

    return time


if __name__ == "__main__":
    assert bestTimeToPartyInterval(sched) == 9
    assert bestTimeToPartyInterval(sched2) == 9.5
    assert bestTimeToPartyInterval(sched3) == 11

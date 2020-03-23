# Programming for the Puzzled -- Srini Devadas
# The Best Time to Party
# Given a list of intervals when celebrities will be at the party
# Output is the time that you want to go the party when the maximum number of
# celebrities are still there.
# Celebrities have weights associated

sched = [(8, 9, 1), (6, 12, 1), (7, 9, 1), (10, 11, 3)]

sched3 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2), (7.0, 8.0, 2), (7.5, 10.0, 3),
          (8.0, 9.0, 2), (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4),
          (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7)]


def bestTimeToPartyWeighted(schedule):
    time = None
    maxcount = 0

    for i, (comes, goes, weight) in enumerate(schedule):
        count = weight
        # Compare to the rest of the list
        for other_comes, other_goes, other_weight in (schedule[:i] + schedule[i+1:]):
            if other_comes <= comes < other_goes:
                count += other_weight

        if count > maxcount:
            maxcount = count
            time = comes

    # Output best time to party
    print('Best time to attend the party is at', time,
          'o\'clock', ':', maxcount, 'weighted celebrities will be attending!')

    return time


assert bestTimeToPartyWeighted(sched) == 10
assert bestTimeToPartyWeighted(sched3) == 11.0

# Just playing around while watching the lecture, before seeing the code
from common import most_frequent

data = [
    ('Beyoncé', 6, 7),
    ('Taylor', 7, 9),
    ('Brad', 10, 11),
    ('Katy', 10, 12),
    ('Tom', 8, 10),
    ('Drake', 9, 11),
    ('Alicia', 6, 8),
]


def best_hour(schedule):
    hours = []
    for person, comes, goes in schedule:
        for h in range(comes, goes):
            hours.append(h)
    return most_frequent(hours)


result = best_hour(data)
print(result)
assert result == 10


# Incremental algorithm
def best_hour_inc(schedule):
    movements = []
    for person, comes, goes in schedule:
        movements.append((comes, 1))
        movements.append((goes, -1))
    movements.sort()
    density = {}
    for hour, change in movements:
        density[hour] = density.get(hour, density.get(hour-1, 0)) + change
    return max(density, key=density.get)


print(best_hour_inc(data))

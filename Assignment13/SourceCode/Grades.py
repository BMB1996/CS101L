import math

def total(values):
    return sum(values)

def average(values):
    if len(values) == 0:
        return math.nan
    elif len(values) > 0:
        return (sum(values) / len(values))

def median(values):
    values.sort()
    try:
        if len(values) == 0:
            raise ValueError
        index = len(values) // 2
        if (len(values) % 2) != 0:
            return values[index]
        else:
            return ((values[index] + values[index - 1]) / 2)
    except ValueError:
        return -1

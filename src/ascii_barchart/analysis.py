from .io import load_rows 

def average_value1_by_type(rows):
    sums = {}
    counts = {}
    for type_, value1, _ in rows:
        sums[type_] = sums.get(type_, 0.0) + value1
        counts[type_] = counts.get(type_, 0) + 1
    return [(t, sums[t] / counts[t]) for t in sorted(sums)]

rows = load_rows("data/points.csv")
averages = average_value1_by_type(rows)
#print(averages)



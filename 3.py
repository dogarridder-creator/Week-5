points = [(2, 5), (8, 3), (4, 4), (9, 1)]

swapped = [(y, x) if x > y else (x, y) for x, y in points]
print(swapped)
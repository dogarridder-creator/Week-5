odometer = (1050, 1085, 1120, 1200, 1215)

segments = [(start, end, end - start) for start, end in zip(odometer[:-1], odometer[1:])]
print(segments)
def field(x1, y1, x2, y2) -> int:
    return (abs(x1-x2)+1) * (abs(y1-y2)+1)

with open("resources/f9_1", 'r') as file:

    points = list()

    max_field = 0

    for l in file:
        points.append([int(x) for x in l.strip().split(',')])

    for p1 in range(len(points)):
        for p2 in range(p1+1, len(points)):
            if max_field < field(points[p1][0], points[p1][1], points[p2][0], points[p2][1]):
                max_field = field(points[p1][0], points[p1][1], points[p2][0], points[p2][1])

    print(max_field)
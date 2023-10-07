def merge(left, right):
    staircase = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        x_left, y_left = left[i]
        x_right, y_right = right[j]

        if x_left <= x_right and y_left >= y_right:
            staircase.append(left[i])
            i += 1
        elif x_left >= x_right and y_left <= y_right:
            staircase.append(right[j])
            j += 1
        else:
            break

    staircase.extend(left[i:])
    staircase.extend(right[j:])

    return staircase

def p(points):
    if len(points) <= 1:
        return points

    mid = len(points) // 2
    leftp = p(points[:mid])
    rightp= p(points[mid:])
    
    return merge(leftp, rightp)


points = [(1, 4), (2, 3), (3, 2), (4, 1), (5, 5), (6, 4), (7, 3), (8, 2)]
result = p(points)

print("Pareto-optimal points :", result)

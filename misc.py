def sign(x: float) -> int:
    if x == 0:
        return 0
    return int(x / abs(x))

def better_range(x: int, y: int = 0, step = 1, inclusive: bool = False) -> range:
    smallerNumber = min(x, y)
    biggerNumber = max(x, y)

    if inclusive:
        biggerNumber += 1

    if step < 0:
        smallerNumber, biggerNumber = biggerNumber, smallerNumber

    return range(smallerNumber, biggerNumber, step)

def manhattan_distance(p1: tuple, p2: tuple) -> float:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def euclidean_distance(p1: tuple, p2: tuple) -> float:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)


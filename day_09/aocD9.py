with open('input.txt') as f:
    file = [instruction.split() for instruction in f.read().splitlines()]

instructions = [[dir[0], int(dir[1])] for dir in file]

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def tail(length):
    knot = [[0,0] for _ in range(length)]
    traversed_coordinates = set()
    traversed_coordinates.add((0,0))

    for direction, steps in instructions:
        for _ in range(steps):
            knot[0][0] += directions[direction][0]
            knot[0][1] += directions[direction][1]

            for i in range(1, len(knot)):
                delta_x = knot[i-1][0] - knot[i][0]
                delta_y = knot[i-1][1] - knot[i][1]

                if max(abs(delta_x), abs(delta_y)) > 1:
                    if delta_x > 0:
                        knot[i][0] += 1
                    elif delta_x == 0:
                        knot[i][0] += 0
                    else:
                        knot[i][0] -= 1

                    if delta_y > 0:
                        knot[i][1] += 1
                    elif delta_y == 0:
                        knot[i][1] += 0
                    else:
                        knot[i][1] -= 1
                    

            traversed_coordinates.add(tuple(knot[-1]))
    
    return len(traversed_coordinates)

print(tail(2))
print(tail(10))


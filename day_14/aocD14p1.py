with open('input.txt') as f:
    lines = f.read().strip().splitlines()

max_y = 0
unique_coors = set()
for line in lines:    
    
    line_coordinates = []

    for coordinates in line.split(' -> '):
        x, y = map(int, coordinates.split(','))
        line_coordinates.append((x, y))
            

    for i in range(1, len(line_coordinates)):

        curr_x, curr_y = line_coordinates[i]
        prev_x, prev_y = line_coordinates[i - 1]

        if curr_y > max_y:
            max_y = curr_y

        if curr_x == prev_x:
            for i in range(min(curr_y, prev_y), max(curr_y, prev_y) + 1):
                unique_coors.add((curr_x, i))

        if curr_y == prev_y:
            for i in range(min(curr_x, prev_x), max(curr_x, prev_x) + 1):
                unique_coors.add((i, curr_y))


def drop_sand():
    x, y = 500, 0
    global unique_coors

    while y <= max_y:
        
        if (x, y + 1) not in unique_coors:
            y += 1
            continue

        if (x - 1, y + 1) not in unique_coors:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in unique_coors:
            x += 1
            y += 1
            continue

        
        unique_coors.add((x, y))
        return True

    return False

counter = 0
while True:
    counter += 1
    drop = drop_sand()

    if not drop:
        break

print(counter - 1)


      
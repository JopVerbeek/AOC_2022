from string import ascii_lowercase
from heapq import heappop, heappush

with open('input.txt') as f:
    heightmap = [[char for char in line] for line in f.read().splitlines()]


l = len(heightmap)
w = len(heightmap[0])

for i in range(l):
    for j in range(w):
        if heightmap[i][j] == 'S':
            start_coor = i, j
        if heightmap[i][j] == 'E':
            end_coor = i, j


def elevation(h):
    if h in ascii_lowercase:
        return ascii_lowercase.index(h)
    if h == 'S':
        return 0
    if h == 'E':
        return 25


def neighbours(i, j):
    for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        rr = r + i
        cc = c + j

        if not (0 <= rr < l and 0 <= cc < w):
            continue

        if elevation(heightmap[rr][cc]) >= elevation(heightmap[i][j]) - 1:
            yield rr, cc


#search algorithm for finding shortest path

visited = set()
heap = [(0, end_coor[0], end_coor[1])]

while True:
    steps, i, j = heappop(heap)
    
    if (i, j) in visited:
        continue    
    visited.add((i, j))

    if elevation(heightmap[i][j]) == 0:
        print(steps)
        break

    for rr, cc in neighbours(i, j):
        heappush(heap, (steps + 1, rr, cc))
    


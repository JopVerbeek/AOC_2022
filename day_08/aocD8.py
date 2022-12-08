import numpy as np

with open('input.txt') as f:
    rows_ = [list(map(int, line)) for line in f.read().splitlines()]    
    columns_ = [[] for _ in range(len(rows_[0]))]


    for i, row in enumerate(rows_):
        for j, col in enumerate(row):
            columns_[j].append(rows_[i][j])


def check_row(i,j, rows):
    value_tree = rows[i][j]
    trees_row = rows[i]    
    left = max(trees_row[:j])
    right = max(trees_row[j+1:])
    
    return value_tree > left or value_tree > right

def check_col(i,j, cols):
    value_tree = cols[j][i]
    trees_col = cols[j]
    up = max(trees_col[:i])
    down = max(trees_col[i+1:])

    return value_tree > up or value_tree > down

def outer_rim(i,j, rows):
    return i == 0 or j == 0 or i == len(rows) - 1 or j == len(rows[0]) - 1

def scenic_score(i,j, rows, cols):
    left_c, right_c, up_c, down_c = 0, 0, 0, 0
    value = rows[i][j]
    trees_row = rows[i]
    trees_col = cols[j]
    left = trees_row[:j][::-1]
    right = trees_row[j+1:]
    up = trees_col[:i][::-1]
    down = trees_col[i+1:]

    for tree in left:
        if tree >= value:
            left_c += 1
            break
        else:
            left_c += 1

    for tree in right:
        if tree >= value:
            right_c += 1
            break
        else:
            right_c += 1

    for tree in up:
        if tree >= value:
            up_c += 1
            break
        else:
            up_c += 1

    for tree in down:
        if tree >= value:
            down_c += 1
            break
        else:
            down_c += 1
            
    return left_c * right_c * up_c * down_c


if __name__ == '__main__':
    #q1
    vis_trees = set()
    for i, row in enumerate(rows_):
        for j, col in enumerate(row):
            if outer_rim(i,j, rows_):
                vis_trees.add((i,j))

            else:
                if check_row(i,j, rows_) or check_col(i, j, columns_):
                    vis_trees.add((i,j))

    print(len(vis_trees))

    #Q2
    all_scores = []
    for i, row in enumerate(rows_):
        for j, col in enumerate(row):
            all_scores.append(scenic_score(i,j, rows_, columns_))

    print(max(all_scores))










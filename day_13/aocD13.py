from ast import literal_eval
from functools import cmp_to_key

with open('input.txt') as f:    
    lines = [par for par in f.read().strip().split('\n\n')]
    

def line_comparison(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return -1
        elif l1 == l2:
            return 0
        else:
            return 1

    elif isinstance(l1, list) and isinstance(l2, list):
        i = 0
        while i < len(l1) and i < len(l2):
            comparison = line_comparison(l1[i], l2[i])
            if comparison == -1:
                return -1
            elif comparison == 1:
                return 1
            
            i += 1

        if i == len(l1) and i < len(l2):
            return -1
        
        elif i == len(l2) and i < len(l1):
            return 1

        else:
            return 0

    elif isinstance(l1, int) and isinstance(l2, list):
        return line_comparison([l1], l2)

    elif isinstance(l1, list) and isinstance(l2, int):
        return line_comparison(l1, [ l2])
        
all_lines = []
counter = 0
for i, line in enumerate(lines):
    l1, l2 = line.split('\n')
    l1, l2 = literal_eval(l1), literal_eval(l2)
    all_lines.append(l1)
    all_lines.append(l2)
    if line_comparison(l1, l2) == -1:
        counter += i+1

print(counter)
#q2 sort all the lines

all_lines.extend([[[2]], [[6]]])


list_sorted = sorted(all_lines, key = cmp_to_key(lambda l1, l2: line_comparison(l1, l2)))
index_seperator_two, index_seperator_six = list_sorted.index([[2]]) + 1, list_sorted.index([[6]]) + 1
print(index_seperator_two * index_seperator_six)

    
      



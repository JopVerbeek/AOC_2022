import re
from copy import deepcopy


##### parser 
with open('input.txt') as f:    
    lines = f.read().split('\n\n')
table = lines[0]
total_stacks = len([line for line in table.splitlines()])
index_lookup = {}
clean_lines = []

for line in table.splitlines():
    line = line.replace('[', ' ').replace(']', ' ')
    clean_lines.append(line)
    counter = 0
    for index, char in enumerate(line):                 
        if len(line.split()) == total_stacks:
            if char != ' ':
                counter += 1
                index_lookup[index] = counter
            
dict_stacks = {num: [] for num in range(1, total_stacks + 1)}

for line in clean_lines:
    for index, char in enumerate(line):
        if index in index_lookup and not char.isdigit():
            dict_stacks[index_lookup[index]].append(char)

values = list(dict_stacks.values())
new_values = []
for row in values:
    list_row = []
    for char in row:
        if char != ' ':
            list_row.append(char)
    new_values.append(list_row[::-1])

final_blocks = dict(zip(dict_stacks.keys(), new_values))
final_blocks_q2 = deepcopy(final_blocks)

### instructions
instructions = [list(map(int,re.findall(r'\d+', line))) for line in lines[1:][0].splitlines()]


def stacking(instructions, final_blocks, method = None):
    for num_crates, departure, destination in instructions:
        if method == 'single':
            corr_crates = final_blocks[departure][-num_crates:][::-1]
            del final_blocks[departure][len(final_blocks[departure]) - num_crates:]
            final_blocks[destination].extend(corr_crates)
        if method == 'stack':
            corr_crates = final_blocks[departure][-num_crates:]
            del final_blocks[departure][len(final_blocks[departure]) - num_crates:]
            final_blocks[destination].extend(corr_crates)

    mess = []
    for k, v in final_blocks.items():
        mess.append(v[-1])

    return ''.join(mess)

print(stacking(instructions, final_blocks, 'single'))
print(stacking(instructions, final_blocks_q2, 'stack'))

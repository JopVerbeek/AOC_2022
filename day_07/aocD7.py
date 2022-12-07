

from collections import Counter

with open('input.txt') as f:
    commands = [line for line in f.read().strip().split('\n') if line]

#Q1

path = []
directories = Counter()
for comm in commands:
    comm = comm.split()
    print(comm)
    
    if comm[1] == 'cd':
        if comm[2] == '..':
            path.pop()
        else:
            path.append(comm[2])

    elif comm[1] == 'ls':
        continue
    else:
        if comm[0].isdigit():
            size = int(comm[0])
            for i, subdir in enumerate(path, 1):
                directories['/'.join(path[:i])] += size

print(sum([v for k, v in directories.items() if v <= 100000]))

#Q2
current_space = 70000000 - max(directories.values())


smallest_feasible_dir = 1000000000000000000000
for k, v in directories.items():
    if current_space + v >= 30000000:
        if v < smallest_feasible_dir:
            smallest_feasible_dir = v

print(smallest_feasible_dir)



        
        


with open('input.txt') as f:
    items = [[letter for letter in line] for line in f.read().splitlines()]


def get_scoring():
    letters_lower = list(map(chr, range(ord('a'), ord('z')+1)))
    letters_upper = [letter.upper() for letter in letters_lower]
    all_letters = letters_lower + letters_upper
    numbers = [num for num in range(1, len(all_letters) + 1)]
    scoring_dict = dict(zip(all_letters, numbers))

    return scoring_dict

def chunks(items, n):    
    for i in range(0, len(items), n):
        yield items[i:i + n]
        
def return_common(left, right):
    return list(set(left).intersection(right))

common = []    
for item in items:
    left_compartment, right_compartment = item[:len(item)//2], item[len(item)//2:]
    common_chars = return_common(left_compartment, right_compartment)
    common.extend(common_chars)

scoring_dict = get_scoring()

counter = 0
for item in common:
    counter += scoring_dict[item]

print(counter)

counter_threes = 0
lists_of_three = list(chunks(items, 3))
for threesome in lists_of_three:
    common = set(threesome[0]).intersection(*threesome)
    counter_threes += scoring_dict[list(common)[0]]

print(counter_threes)



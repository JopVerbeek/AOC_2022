with open('input.txt') as f:
    monkeys = [paragraph.strip().splitlines() for paragraph in f.read().strip().split('\n\n')]
   
list_items, operations, tests, true_monkey, false_monkey = [], [], [], [], []


for monkey_attr in monkeys:
    items = list(map(int, monkey_attr[1].split(':')[1].split(',')))  
    list_items.append(items)      
    operation = monkey_attr[2].split('=')[1].split(" ")[-2:]
    operations.append(operation)
    test = int(monkey_attr[3].split(' ')[-1:][0])
    
    tests.append(test)
    monkey_true = int(monkey_attr[4].split(' ')[-1][0])
    true_monkey.append(monkey_true)
    monkey_false = int(monkey_attr[5].split(' ')[-1][0])
    false_monkey.append(monkey_false)

hcd = 1
for num in tests:
    hcd *= num

def monkey_business(runs, q = None):
    monkey_counts = [0 for monkey in range(len(monkeys))]
    for _ in range(runs):
        for i in range(len(monkeys)):  
            
            for worry_level in list_items[i]:
                monkey_counts[i] += 1
                operation, num = operations[i]
                if num.isdigit():
                    num = int(num)
                else:
                    num = worry_level
                
                if operation == '*':
                    new_worry_level = worry_level * num
                elif operation == '+':
                    new_worry_level = worry_level + num

                if q == 1:
                    final_worry_level = new_worry_level // 3
                elif q == 2:
                    final_worry_level = new_worry_level % hcd
                

                if final_worry_level % tests[i] == 0:
                    list_items[true_monkey[i]].append(final_worry_level)
                else:
                    list_items[false_monkey[i]].append(final_worry_level)

            list_items[i] = []

    sort_monkey_counts = sorted(monkey_counts)
    ans = sort_monkey_counts[-1] * sort_monkey_counts[-2]
    return ans

if __name__ == '__main__':
    print(monkey_business(20,q=1))
    print(monkey_business(10000, q=2))



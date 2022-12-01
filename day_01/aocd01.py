with open('input.txt') as f:
    lines = [block.split('\n') for block in f.read().split('\n\n') if block]    
nums = [sum(list(map(int,[num for num in block if num]))) for block in lines]
sorted_nums = sorted(nums)
top_3 = sum(sorted_nums[-3:])
print(max(nums))
print(top_3)
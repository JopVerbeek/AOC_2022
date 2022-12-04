with open('input.txt') as f:
    sections = [line.split(',') for line in f.read().splitlines()]
    sections_ = [[list(map(int, sec.split('-'))) for sec in line] for line in sections]
    print(sections_)
    
def overlapping(list_nums):
    range1, range2 = list_nums[0], list_nums[1]
    
    nums1 = [num for num in range(range1[0], range1[1] + 1)]
    nums2 = [num for num in range(range2[0], range2[1] + 1)]

    resultQ1 = all(elem in nums1 for elem in nums2) or all(elem in nums2 for elem in nums1)
    resultQ2 = any(elem in nums1 for elem in nums2) or any(elem in nums2 for elem in nums1)

    return resultQ1, resultQ2

counterQ1 = 0 
counterQ2 = 0
for section in sections_:
    q1, q2 = overlapping(section)
    if q1:
        counterQ1 += 1
    if q2:
        counterQ2 += 1

print(counterQ1)
print(counterQ2)
        

    
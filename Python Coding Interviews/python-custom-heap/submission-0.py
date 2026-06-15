import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    c=[]
    d=[]
    for num in nums:
        c.append(((-num),num))
    heapq.heapify(c)
    #print(c,'l')
    while c:
        top=heapq.heappop(c)
        d.append(top[1])
    return d



    pass



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

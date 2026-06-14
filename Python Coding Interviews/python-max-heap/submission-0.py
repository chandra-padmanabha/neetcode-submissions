import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    nums_negated=[-num for num in nums]
    heapq.heapify(nums_negated)
    c=[]
    while nums_negated:
        top=heapq.heappop(nums_negated)
        c.append(-top)
    return c
    pass





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

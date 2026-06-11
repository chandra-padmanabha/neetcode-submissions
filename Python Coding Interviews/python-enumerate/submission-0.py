from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i,num in enumerate(nums):
        if num==7 :
            return i
        elif i==len(nums)-1 and num!=7:
            return -1
            
    pass


def get_dist_between_sevens(nums: List[int]) -> int:
    count=0
    for i,num in enumerate(nums):
        if num==7 and count==0:
            count+=i+1
        elif num==7 and count>0:
            return i-count+1

        

    pass


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        twoSum={}
        for i,n in enumerate(numbers):
            diff=target-n
            if diff in twoSum:
                return [twoSum[diff]+1,i+1]
            twoSum[n]=i




        
from typing import List


class Solution:
    def singleNumber(self,nums:List[int])->int:
        for val in set(nums):
            if nums.count(val)==1:
                return val

if __name__=="__main__":
    t=Solution()
    print(t.singleNumber(nums = [2,2,1]))
#https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def misssingNumber(self,nums:List[int])->int:
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return i+1

if __name__=="__main__":
    t=Solution()
    print(t.misssingNumber(nums = [9,6,4,2,3,5,7,0,1]))
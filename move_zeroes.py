#https://leetcode.com/problems/move-zeroes/solution/
from typing import List


class Solution:
    def moveZeroes(self,nums:List[int])->None:
        for i in range (nums.count(0)):
            nums.remove(0)
            nums.append(0)

if __name__=="__main__":
    t=Solution()
    t.moveZeroes(nums = [0,1,0,3,12])
#https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self,nums:List[int])->bool:
        #Naive solution
        # for val in set(nums):
        #     if nums.count(val)>1:
        #         return True
        # return False
        return len(set(nums)) != len(nums)
if __name__=="__main__":
    t=Solution()
    print(t.containsDuplicate(nums = [1,2,3,1]))
    print(t.containsDuplicate(nums = [1,2,3,4]))
#https://leetcode.com/problems/majority-element/

from typing import List


class Soluton:
    def majorityElement(self,nums:List[int])->int:
        for val in set(nums):
            if (nums.count(val)) > (len(nums)/2):
                return val


if __name__=="__main__":
    t=Soluton()
    print(t.majorityElement(nums = [3,2,3]))

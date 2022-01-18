#kadane Algorithm

from typing import List
from queue import Queue

class Solution():
    def maxSubarray(self,nums:List[int])->int:
        currsum=maxValue=nums[0]
        for i in range (1,len(nums)):
            currPos=nums[i]
            currsum=max(currPos,currPos+currsum)
            maxValue=max(currsum,maxValue)
        return maxValue
            
from typing import List


class Solution:
    def removeDuplicates(self,nums:List[int])->int:
        # i=0
        # j=1
        # if len(nums)==0 or len(nums)==1:
        #     return None
        # while j<len(nums):
        #     if nums[i]==nums[j]:
        #         j+=1
        #     else:
        #         i+=1
        #         nums[i]=nums[j]
            
        # return i+1
        n=set(nums)
        nums=list(n)
        print(nums)
        return len(nums)
if __name__=="__main__":
    t=Solution()
    print(t.removeDuplicates([1,1,2]))
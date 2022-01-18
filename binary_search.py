#https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums, target: int)->int:
        def binarySearch(arr,start,end,target):
            if end>=start:
                mid=(start+end)//2
                if arr[mid]==target:
                    return mid
                
                elif arr[mid]>target:
                    return binarySearch(arr,start,mid-1,target)
                
                else:
                    return binarySearch(arr,mid+1,end,target)

            else:
                return -1
        
        return binarySearch(nums,0,len(nums)-1,target)


if __name__=="__main__":
    t=Solution()
    print(t.search(nums = [-1,0,3,5,9,12], target = 9))
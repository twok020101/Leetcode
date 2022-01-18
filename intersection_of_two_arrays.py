#https://leetcode.com/problems/intersection-of-two-arrays-ii/
from typing import List


class Solution:
    def intersect(self, nums1: List[int],nums2: List[int])->List[int]:
        nums1.sort()
        nums2.sort()
        final_array=[]
        n,m=len(nums1),len(nums2)
        i,j=0,0
        while (i<n) and (j<m):
            if nums1[i]==nums2[j]:
                final_array.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return final_array

if __name__=="__main__":
    t=Solution()
    print(t.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))

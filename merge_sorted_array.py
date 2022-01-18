from typing import List


class Solution:
    def merge(self,nums1:List[int],m:int,nums2:List[int],n:int)->None:
        nums1=nums1[:m]
        i=0
        j=0
        while(i<m and j<n):
            if (nums2[j]<=nums1[i]):
                nums1.insert(i,nums2[j])
                j+=1
            else:
                i+=1
        while(j!=n):
            nums1.append(nums2[j])
            j+=1
        print(nums1)

if __name__=="__main__":
    t=Solution()
    t.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
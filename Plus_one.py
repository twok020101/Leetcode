from typing import List


class Solution:
    def plusOne(self,digits:List[int])->List[int]:
        n=len(digits)
        number=0
        itr=0
        for i in range(n-1,-1,-1):
            number+=(digits[itr]*pow(10,i))
            itr+=1
        final=list(map(int,str(number+1)))
        return final

if __name__=="__main__":
    t=Solution()
    print(t.plusOne([4,3,2,1]))
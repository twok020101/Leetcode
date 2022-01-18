from typing import List


class Solution:
    def generate(self,numsRows:int)->List[List[int]]:
        out=[[] for i in range(numsRows)]
        out[0].append(1)
        if numsRows==1:
            return out
        for i in range (1,numsRows):
            currValue=0
            for j in range (i):
                out[i].append(currValue+out[i-1][j])
                currValue=out[i-1][j]
            out[i].append(1)
        return out

if __name__=="__main__":
    t=Solution()
    print(t.generate(5))

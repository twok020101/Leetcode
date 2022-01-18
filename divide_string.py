from typing import List
import textwrap


class Solution:
    def divideString(self, s: str,k: int,fill:str)->List[str]:
        if len(s)%k==0:
            return textwrap.wrap(s,k)
        else:
            fact=k-(len(s)%k)
            s+=(fill*fact)
            return textwrap.wrap(s,k)


if __name__=="__main__":
    t=Solution()
    print(t.divideString(s = "abcdefghij", k = 3, fill = "x"))
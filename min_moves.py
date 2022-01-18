class Solution:
    def minMoves(self, target: int, maxDoubles: int)->int:
        moves=0
        while (target!=1 and maxDoubles!=0):
            # print(target)
            if target%2==0:
                target=target//2
                maxDoubles-=1
                moves+=1
                continue
            target-=1
            moves+=1

        if target!=1:
            moves+=(target-1)
        
        return moves

if __name__=="__main__":
    t=Solution()
    print(t.minMoves(target = 19, maxDoubles = 2))
class Solution:
    def wordPattern(self, pattern: str, s: str)->bool:
        pattern=[char for char in pattern]
        s=s.split()
        di={}
        for i in range(len(set(pattern))):
            di[pattern[i]]=s[i]
        if len(di.values())!=len(set(di.values())):
            return False
        for i,let in enumerate(pattern):
            if di[let]!=s[i]:
                return False
        
        return True

if __name__=="__main__":
    t=Solution()
    print(t.wordPattern("abba","dog dog dog dog"))
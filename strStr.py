class Solution:
    def strStr(self,haystack:str, needle:str)->int:
        if needle in haystack:
            return haystack.find(needle)
        return -1

if __name__=="__main__":
    t=Solution()
    print(t.strStr(haystack = "", needle = ""))
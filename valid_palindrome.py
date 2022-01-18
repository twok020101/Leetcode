class Solution:
    def isPalindrome(self, s:str)->bool:
        s=(''.join(ch for ch in s if ch.isalnum())).strip().lower()
        print(s)
        n=len(s)
        print(n)
        print(s[:n//2], s[n-1:n//2:-1], n//2)
        if n%2==1:
            if s[:n//2]==s[n-1:(n//2):-1]:
                return True
        else:
            if s[:n//2]==s[n-1:(n//2)-1:-1]:
                return True
        return False


if __name__=="__main__":
    t=Solution()
    print(t.isPalindrome(s = "0P"))
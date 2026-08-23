class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join([ch.lower() for ch in s if ch.isalnum()])
        print(clean)
        if clean == clean[::-1]:
            return True
        else:
            return False
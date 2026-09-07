class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)

        def expand(l: int, r: int) -> tuple[int]:
            while l >= 0 and r < len_s and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r - 1)

        left, right = 0, 0
        for i in range(len_s - 1):
            for l, r in [(i, i), (i, i + 1)]:
                new_l, new_r = expand(l, r)
                if new_r - new_l > right - left:
                    left, right = new_l, new_r
        return s[left: right + 1]

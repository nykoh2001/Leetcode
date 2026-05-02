"""https://leetcode.com/problems/longest-common-prefix/description/

- 최장 공통 prefix
- 문자열 하나 잡고 모든 부분 prefix 구해서 차례대로 다른 문자열들의 부분수열인지 아닌지?
- O(N x M)

- zip을 활용하는 경우도 존재
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot_str = strs[0]
        prefix = ""
        for char in pivot_str:
            current_prefix = prefix + char
            if all(str.startswith(current_prefix) for str in strs[1:]):
                prefix += char
            else:
                return prefix
        
        return prefix

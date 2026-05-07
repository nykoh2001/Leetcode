"""https://leetcode.com/problems/top-k-frequent-elements/description/

- Counter -> 최빈값 구하기
"""

from typing import List
from collections import Counter, defaultdict


class Solution:
    def _topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        N: len(nums)
        M: number of unique frequencies
        """
        # O(N)
        counter = Counter(nums)

        reversed_counter = defaultdict(list)
        # O(N)
        for key, value in counter.items():
            reversed_counter[value].append(key)

        # O(N)
        top_frequent_counter = sorted(reversed_counter.items(), key=lambda x: -x[0])

        top_k_values = []
        # O(N)
        while top_frequent_counter and len(top_k_values) < k:
            _, values_to_append = top_frequent_counter[0]
            top_k_values.extend(values_to_append)
            del top_frequent_counter[0]

        return top_k_values[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N)
        counter = Counter(nums)

        # O(N x N logN)
        return [k for k, _ in counter.most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Even better: O(N logN)
        """
        freq = defaultdict(int)

        # O(N)
        for num in nums:
            freq[num] += 1

        # O(N log N)
        f = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]

        # O(N)
        ans = [num for num, _ in f]
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))

"""https://leetcode.com/problems/two-sum/description/

Problem:
주어진 배열의 임의의 두 수의 합이 타겟 숫자가 되는 숫자 조합들의 인덱스 출력

- 브루트포스: 모든 2개 숫자 조합의 sum을 구하고 타겟 넘버가 나오면 return
  - O(N^2)
- Dict에 값을 인덱스로, 인덱스를 값으로 하도록 초기화
  - O(N)
"""

from typing import List
from collections import defaultdict

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         len_num = len(nums)
#         for i in range(len_num):
#             for j in range(i + 1, len_num):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dict = defaultdict(list)
        for i, num in enumerate(nums):
            number_dict[num].append(i)

            if num == target - num:
                if number_dict[num] and len(number_dict[num]) >= 2:
                    target_number_comb = number_dict[num]
                    return sorted(target_number_comb[:2])
                continue

            another_num_idx = number_dict.get(target - num)
            if another_num_idx and another_num_idx[0] is not None:
                return sorted([i, another_num_idx[0]])


if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum([2, 7, 11, 15], 9)
    print(result)

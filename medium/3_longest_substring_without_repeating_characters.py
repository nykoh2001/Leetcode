"""https://leetcode.com/problems/longest-substring-without-repeating-characters/

- two pointer, start & end
- str[start:end]
  - end += 1: if no duplicate letter
  - start += 1: if duplicate letter found
  - max_length
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        start_idx, end_idx = 0, min(len_s, 1)
        letter_count = set()

        # Initialize
        letter_count.update(s[start_idx:end_idx])
        max_length = end_idx - start_idx

        # O(N)
        while end_idx < len_s:
            # If last letter is duplicate, increase start idx to move to the next substring
            if s[end_idx] in letter_count:
                letter_count.remove(s[start_idx])
                start_idx += 1
                continue

            # If substring includes only unique letters, increase end idx to expand substring
            letter_count.add(s[end_idx])
            end_idx += 1

            # Update max substring length
            max_length = max(max_length, end_idx - start_idx)
            # print(
            #     f"current substring: {s[start_idx:end_idx]}, counter: {letter_count} max_length: {max_length}"
            # )

        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("au"))

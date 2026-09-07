class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n + 1):
            one_count = 0
            while num > 0:
                num = num & (num - 1)
                one_count += 1
            result.append(one_count)
        return result

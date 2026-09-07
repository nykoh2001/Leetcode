class Solution:
    def findIntegers(self, n: int) -> int:
        binary = bin(n)[2:]
        if len(binary) == 1:
            return 2
        dp = [0] * (len(binary) + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, len(binary) + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        answer = 0
        prev_bit = 0
        for i in range(len(binary) - 1, -1, -1):
            if n & (1 << i):
                answer += dp[i]

                if prev_bit == 1:
                    return answer

                prev_bit = 1
            else:
                prev_bit = 0
        return answer + 1

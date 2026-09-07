class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for _ in range(32):
            bit = n & 1
            answer = (answer << 1) | bit
            n = n >> 1
        return answer

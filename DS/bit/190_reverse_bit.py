class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = bin(n)[2:]
        padding_length = 32 - len(binary_string)
        binary_int = int(binary_string[::-1], 2)
        binary_int = binary_int << padding_length
        return binary_int

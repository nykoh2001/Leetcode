"""https://leetcode.com/problems/valid-parentheses/description/

- stack 선언
- 왼쪽 괄호면 push, 오른쪽 괄호면 pop

--- Better solution ---
dic = {')': '(', '}': '{', ']':'['}
"""

class Paranthese:
    LEFT_SMALL = "("
    RIGHT_SMALL = ")"

    LEFT_MEDIUM = "{"
    RIGHT_MEDIUM = "}"

    LEFT_LARGE = "["
    RIGHT_LARGE = "]"


def validate(left, right) -> bool:
    if (
        (left == Paranthese.LEFT_SMALL and right == Paranthese.RIGHT_SMALL)
        or (left == Paranthese.LEFT_MEDIUM and right == Paranthese.RIGHT_MEDIUM)
        or (left == Paranthese.LEFT_LARGE and right == Paranthese.RIGHT_LARGE)
    ):
        return True
    return False


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []

        right_parenthesis = [
            Paranthese.RIGHT_LARGE,
            Paranthese.RIGHT_MEDIUM,
            Paranthese.RIGHT_SMALL,
        ]
        left_parenthesis = [
            Paranthese.LEFT_LARGE,
            Paranthese.LEFT_MEDIUM,
            Paranthese.LEFT_SMALL,
        ]
        for char in s:
            if char in left_parenthesis:
                parentheses.append(char)
            elif char in right_parenthesis:
                if not parentheses:
                  return False
                left_parentheses = parentheses.pop()
                is_valid = validate(left_parentheses, char)
                if not is_valid:
                    return False

        if len(parentheses):
            return False

        return True

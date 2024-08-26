class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        final = ''
        while columnNumber > 0:
            columnNumber -= 1
            order = columnNumber % 26
            final = chr(order + 65) + final
            columnNumber //= 26
        return final
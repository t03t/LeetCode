class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = []
        for s in address:
            if s == '.':
                answer.append("[.]")
            else:
                answer.append(s)
        return "".join(answer)
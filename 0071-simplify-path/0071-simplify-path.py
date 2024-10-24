class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for fileName in path.split('/'):
            if not fileName:
                continue
            if fileName == ".." and stack:
                stack.pop()
            elif fileName == ".." or fileName == ".":
                continue
            else:
                stack.append(fileName)
        return '/'+'/'.join(stack)
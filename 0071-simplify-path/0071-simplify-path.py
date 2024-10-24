class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        print(path.split('/'))
        for fileName in path.split('/'):
            if not fileName:
                continue
            print(fileName)
            ##
            if fileName == ".." and stack:
                stack.pop()
            elif fileName == ".." or fileName == ".":
                continue
            else:
                stack.append(fileName)
        print(stack)
        return '/'+'/'.join(stack)
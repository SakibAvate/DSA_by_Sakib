class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        unmatched = 0

        for ch in s:
            if ch == '(':
                stack.append(ch)

            elif stack:
                stack.pop()

            else:
                unmatched +=1

        return len(stack)+ unmatched                
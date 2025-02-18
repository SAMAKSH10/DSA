class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = ""
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))  # Push numbers in order
            if i == len(pattern) or pattern[i] == 'I':  
                while stack:
                    result += stack.pop()  # Pop when 'I' is found
        return result

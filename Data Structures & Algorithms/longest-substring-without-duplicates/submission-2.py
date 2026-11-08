class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        stack = {}
        stack_cursor = 0
        for idx, char in enumerate(s):
            if char in stack:
                new_stack_cursor = stack[char] + 1
                for deleting_idx in range(stack_cursor, new_stack_cursor-1):
                    del stack[s[deleting_idx]]
                stack[char] = idx
                stack_cursor = new_stack_cursor
            else:
                stack[char] = idx
                current_length = idx - stack_cursor + 1
                if  current_length > longest:
                    longest = current_length
        
        return longest
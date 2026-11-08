class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile(r'[^a-zA-Z0-9]')
        cleaned_lower = pattern.sub('', s).lower()
        return cleaned_lower == cleaned_lower[::-1] 
        
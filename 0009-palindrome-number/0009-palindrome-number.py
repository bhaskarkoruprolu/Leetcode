class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        x_str = str(x)
        
        # Check if the string is the same as its reverse
        return x_str == x_str[::-1]
        
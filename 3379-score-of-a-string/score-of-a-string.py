class Solution:

    # the time complexity of this solution is O(n)
    
    def scoreOfString(self, s: str) -> int:
        total_sum = 0
        for index in range(len(s) - 1): # -1 because we don't want to go to the end of the loop
            current_char_ascii_val = ord(s[index])
            next_char_ascii_val = ord(s[index + 1])

            difference = abs(current_char_ascii_val - next_char_ascii_val)
            total_sum += difference
        
        return total_sum
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_list = { 
            'I' : 1, 
            'V' : 5, 
            'X' : 10, 
            'L' : 50, 
            'C' : 100, 
            'D' : 500, 
            'M' : 1000
        }
        sum=0
        for i in range(len(s)):
            sum += roman_list[s[i]]
            if roman_list[s[i]] > roman_list[s[i-1]] and i > 0:
                sum -= roman_list[s[i-1]]*2
        return sum

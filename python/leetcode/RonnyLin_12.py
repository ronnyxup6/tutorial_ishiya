class Solution:
    def intToRoman(self, num: int) -> str:
        roma_num = ""
        roma_list = ['I','V','X','L','C','D','M']
        i = 0
        while (num > 0):
            a = int(num % 10)
            if a < 4:
                roma_num = roma_list[i]*a + roma_num
            elif a == 4:
                roma_num = roma_list[i] + roma_list[i+1] + roma_num
            elif (a < 9) and (a > 4):
                roma_num = roma_list[i+1] + roma_list[i]*(a-5) + roma_num
            elif a == 9:
                roma_num = roma_list[i] + roma_list[i+2] + roma_num
            i += 2
            num = num // 10
            
        return roma_num
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        for i in range(1,len(strs)):
            for j in range(len(a)):           
                if j+1 > len(strs[i]) :
                    a = a[:j]
                    break
                if a[j] != strs[i][j]:
                    a = a[:j]
                    break
        return a
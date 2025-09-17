class Solution:
    def reversestring(self,str):
        left = 0
        right = len(str)-1
        while left < right:
            str[left],str[right]=str[right],str[left]
            left+=1
            right-=1
        
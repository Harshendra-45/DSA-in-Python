class Solution(object):

    def isPalindrome(self, s):
        p="!@#$%^&*(){}[]\_-:;,`.?'/\""
        s=s.replace(" ","")
        s=s.lower()
        for i in p:
            s=s.replace(i,"")
        return s==s[::-1]
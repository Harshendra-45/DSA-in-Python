class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        s1=""
        for i in word1:
            s1+=i
        s2=""
        for i in word2:
            s2+=i
        return s1==s2

        
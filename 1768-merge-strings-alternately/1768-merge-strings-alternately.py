class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res=""
        minl =min(len(word1),len(word2)) 
        for i in range(minl):
            res+=word1[i]
            res+=word2[i]
        if len(word1)>len(word2):
            res+=word1[i+1:]
        else:
            res+=word2[i+1:]
        return res

        
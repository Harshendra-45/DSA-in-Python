class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
      z = s.split()
      res=""
      for i in range(k):
        res+=z[i]
        res+=" "
      return res[:-1]
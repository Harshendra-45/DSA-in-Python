class Solution(object):
    def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            # s = input("Enter a string: ")
            res=""
            temp=""
            for i in s:
                if i not in temp:
                    temp=temp+i
                    # print(temp)
                else:
                    if len(temp)>len(res):
                        res=temp
                    temp = temp[temp.find(i)+1:]
                    
                    temp= temp+i
                        #  print(temp)
            if len(temp)>len(res):
                res = temp


            # print(res)
            return len(res)
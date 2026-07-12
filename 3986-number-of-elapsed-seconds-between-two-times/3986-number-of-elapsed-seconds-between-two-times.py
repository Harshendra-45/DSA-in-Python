class Solution(object):
    def secondsBetweenTimes(self, starttime, endtime):
        end = int(endtime[0:2])*3600+int(endtime[3:5])*60+int(endtime[6:])
        start = int(starttime[0:2])*3600+int(starttime[3:5])*60+int(starttime[6:])
        return end-start
        
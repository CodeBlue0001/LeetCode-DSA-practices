class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # print(sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31]))
        aa=sum(days[: int(arriveAlice[:2])-1]) + int(arriveAlice[3:])
        ad=sum(days[: int(leaveAlice[:2]) -1] ) + int(leaveAlice[3:])
        
        print(aa,ad)

        ba=sum(days[: int(arriveBob[:2])-1] ) + int(arriveBob[3:])
        bd=sum(days[: int(leaveBob[:2]) -1]  ) + int(leaveBob[3:])

        print(ba,bd)

        start=max(aa,ba)
        end=min(bd,ad)
        
        if start<=end:
            return end-start+1
        else:
            return 0
        

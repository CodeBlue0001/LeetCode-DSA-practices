class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        ans=[0]*n
        previous=0
        stack=[]

        for log in logs:
            pid,op,time_stamp=log.split(":")
            pid=int(pid)
            time_stamp=int(time_stamp)
            if op=='start':
                if stack:
                    ans[stack[-1]]+=time_stamp-previous
                
                stack.append(pid)
                previous=time_stamp
            else:
                ans[stack.pop()]+=time_stamp-previous+1
                previous=time_stamp+1
        return ans
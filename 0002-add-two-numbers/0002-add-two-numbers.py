# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def find_num(ptr):
            n=""
            while ptr!=None:
                n+=str(ptr.val)
                ptr=ptr.next
            return int(n[::-1])
        n1=find_num(l1)
        n2=find_num(l2)
        result=n1+n2
        # print(f"{n1}+{n2}={result}")
        result=str(result)[::-1]
        # print(result)
        # updating the l1
        i=0
        ptr=l1
        prv=None
        while ptr:
            ptr.val=int(result[i])
            prv=ptr
            ptr=ptr.next
            i+=1
        # print(i)
        # adding extra digits if they are left 
        while i<=len(result)-1:
           prv.next=ListNode(int(result[i]))
           i+=1
           prv=prv.next 

        return l1

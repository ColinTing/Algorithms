class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        while l1 is None and l2 is not None:
            return l2
        while l1 is not None and l2 is None:
            return l1
        while l1 is None and l2 is None:
            return None

        dummy = ListNode(0)
        dummy.next = l1
        cur = l1
        pre = dummy
        while cur is not None and l2 is not None:
            if cur.val<l2.val:
                pre = cur
                cur = cur.next
            else:
                temp = cur
                cur = ListNode(l2.val)
                pre.next = cur
                cur.next = temp
                l2 = l2.next
        if l2 is not None:
            cur = l2
            pre.next = cur
        return dummy.next

    def printListNode(self, listNode):
        answer = []
        head  = listNode
        while head is not None:  #这里没有 head.next 的判断，那么上面的 cur 需要么？ 需要，因为会比对cur和cur.next的值
            answer.append(head.val)
            head = head.next
        return answer



l1 = ListNode(-9)
l1.next = ListNode(3)
#l1.next.next = ListNode(4)

l2 = ListNode(5)
l2.next = ListNode(7)
#l2.next.next = ListNode(4) 


s = Solution()
list = s.mergeTwoLists(l1, l2)
print(s.printListNode(list))
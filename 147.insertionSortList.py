class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


list = ListNode(-1, ListNode(5, ListNode(3, ListNode(
    4, ListNode(0)))))


class Solution:
    def insertionSortList(self, head):
        
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        #pre = dummy    #pre可省略
        cur = head
        while cur is not None and cur.next is not None:
            if cur.val < cur.next.val:
                cur = cur.next
            else:
                temp = cur.next
                cur.next = temp.next
                pre = dummy
                #head = dummy.next  #head可省略
                while temp.val>pre.next.val:  #head 替换成 pre 时可以只用一个pre 来实现排序，因为他是对pre.next进行操作
                    pre = pre.next            #head 而用head操作时需要两个参数 并且在while循环中还需要  *pre = head* head = head.next
                temp.next = pre.next
                pre.next = temp
        return dummy.next
        
        

        
    def printListNode(self, listNode):
        answer = []
        head  = listNode
        while head is not None:  #这里没有 head.next 的判断，那么上面的 cur 需要么？ 需要，因为会比对cur和cur.next的值
            answer.append(head.val)
            head = head.next
        return answer


s = Solution()
s.insertionSortList(list)
print(s.printListNode(list))

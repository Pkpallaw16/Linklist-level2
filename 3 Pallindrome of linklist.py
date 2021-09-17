def mid_of_linklist(node):
    slow=node
    fast = node.next
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_linklist(node):
    prev=None
    cur=node
    while cur!=None:
        temp=cur.next
        cur.next=prev
        prev=cur
        cur=temp
    return prev
def pallindrome_of_linklist(node):
    first=node
    mid=mid_of_linklist(node)
    second=mid.next
    mid.next=None
    while first!=None and second!=None:
        if first.val!=second.val:
            return False
        first=first.next
        second=second.next
    return True
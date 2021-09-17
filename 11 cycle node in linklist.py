def hasCycle(node):
    slow=node
    fast=node
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    if fast==None or fast.next==None:
        return None
    slow=node
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return slow
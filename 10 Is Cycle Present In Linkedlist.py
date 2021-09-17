def hasCycle(node):
    slow=node
    fast=node
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
        return False
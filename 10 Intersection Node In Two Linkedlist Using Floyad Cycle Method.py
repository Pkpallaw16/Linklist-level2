def Cycle_node(node):
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

def getIntersectionNode(head1,head2):
    tail=head1
    while tail.next!=None:
        tail=tail.next
    tail.next=head1
    res=Cycle_node(head2)
    tail.next=None
    return res
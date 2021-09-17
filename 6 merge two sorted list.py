"""1->2->6->7->15->24->null
-1->0->6->17->25->null"""
def merge_two_sorted_list(node1,node2):
    dummy=Node(0)
    temp=dummy
    while node1!=None and node2!=None:
        if node1.val<node2.val:
            dummy.next=node1
            node1=node1.next
        else:
            dummy.next = node2
            node2 = node2.next
    if node1!=None:
        dummy.next=node1
    else:
        dummy.next=node2
    return temp.next


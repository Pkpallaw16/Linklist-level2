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
def merge_k_list(lists,start,end):
    if start==end:
        return lists[start]
    mid=int((start+end)/2)
    l1=merge_k_list(lists,start,mid)
    l2=merge_k_list(lists,mid+1,end)
    return merge_two_sorted_list(l1,l2)
def mergeKLists(lists):
    return merge_k_list(lists,0,len(lists)-1)
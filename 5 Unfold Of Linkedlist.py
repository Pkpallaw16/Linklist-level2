def reverse_linklist(node):
    prev=None
    cur=node
    while cur!=None:
        temp=cur.next
        cur.next=prev
        prev=cur
        cur=temp
    return prev
def Unfold_Of_Linkedlist(node):
    if node == None or node.next==None or node.next.next==None:
        return
    odd_head=Node(-1)
    even_head=Node(-1)
    t1=odd_head
    t2=even_head
    indx=0
    cur=node
    while cur!=None:
        if indx%2==0:
            t2.next=cur
            t2=t2.next
        else:
            t1.next=cur
            t1=t1.next
    t1.next=None
    t2.next=None
    odd_head=reverse_linklist(odd_head.next)
    t2.next=odd_head
    return even_head.next
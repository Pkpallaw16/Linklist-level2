def segregate012(head):
    head0=Node(-1)
    head1=Node(-1)
    head2=Node(-1)
    t0=head0
    t1=head1
    t2=head2
    temp=head
    while temp!=None:
        if temp.val==0:
            t0.next=temp
            t0=temp
        elif temp.val==1:
            t1.next=temp
            t1=temp
        else:
            t2.next=temp
            t2=temp
        temp=temp.next
    t2.next=None
    t1.next=head2.next
    t0.next=head1.next
    return head0.next

def segregate012_2nd(head):
    cur=head  #first unsolved
    head1=head #first 1
    head2=head #first 2
    while cur !=None:
        if cur.val==2:
            cur=cur.next
        elif cur.val==1:
            head2.val, cur.val = cur.val, head2.val
            head2 = head2.next
            cur = cur.next
        else:
            head2.val,cur.val=cur.val,head2.val
            head2.val, head1.val = head1.val, head2.val
            head1=head1.next
            head2=head2.next
            cur=cur.next
    return head
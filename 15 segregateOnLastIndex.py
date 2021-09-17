def segregateOnLastIndex(head):
    pivot=head
    while pivot.next!=None:
        pivot=pivot.next
    smaller=Node(-1)
    greater=Node(-1)
    t1=smaller
    t2=greater
    temp=head
    while temp!=None:
        if temp.val<=pivot.val:
            t1.next=temp
            t1=temp
        else:
            t2.next=temp
            t2=temp
        temp=temp.next
    t2.next=None
    t1.next=greater.next
    return pivot
def segregateOnGivenIndex(head,pivotIdx):
    pivot=head
    for i in range(pivotIdx):
        pivot=pivot.next
    smaller=Node(-1)
    greater=Node(-1)
    t1=smaller
    t2=greater
    temp=head
    while temp!=None:
        if pivot!=temp:
            if temp.val<=pivot.val:
                t1.next=temp
                t1=temp
            else:
                t2.next=temp
                t2=temp
        temp=temp.next
    t2.next=None
    pivot.next=greater.next
    t1.next=pivot
    return smaller.next
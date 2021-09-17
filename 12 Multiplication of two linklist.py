thead=None
ttail=None
def addFirst(node):
    global thead, ttail
    if thead==None:
        thead=ttail=node
    else:
        node.next=thead
        thead=node
def reverseUsingAddFirst(head):
    cur=head
    while cur!=None:
        node=cur
        cur=node.next
        node.next=None
        addFirst(node)
    return thead
def add_two_list(one,two):
    one=reverseUsingAddFirst(one)
    two=reverseUsingAddFirst(two)
    p1=one
    p2=two
    carry=0
    while p1!=None or p2 !=None or carry!=0:
        if p1==None:
            val1=0
        else:
            val1=p1.data
            p1=p1.next
        if p2==None:
            val2=0
        else:
            val2=p2.data
            p2=p2.next
        sum=val1+val2+carry
        val=sum%10
        carry=int(sum/10)
        addFirst(val)
    return thead
def multiplyTwoLL(l1,l2):
    l1 = reverseUsingAddFirst(l1)
    l2 = reverseUsingAddFirst(l2)
    res=None
    zero_count=0
    t1=l1
    while t1!=None:
        #number which we have to add in res
        num=Node(-1)
        k=num
        for z in range(zero_count):
            node=Node(0)
            k.next=node
        t1_val=t1.val
        t1= t1.next
        t2=l2
        carry=0
        while carry!=0 or t2!=None:
            if t2==None:
                t2_val=0
                t2=None
            else:
                t2_val=t2.val
                t2=t2.next
                prod=t1_val*t2_val+carry
                val=Node(prod%10)
                carry=int(prod/10)
                k.next=val
                k=val
        res=add_two_list(res,num.next)
        zero_count+=1
    res=reverseUsingAddFirst(res)
    return res



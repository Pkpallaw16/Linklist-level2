class Node:
    def __init__(self,val=0,next=None,random=None):
        self.val=val
        self.next=next
        self.random=random
def display(head):
    temp=head
    while temp!=None:
        print("(",temp.val,end="->")
        if temp.random!=None:
            print(temp.random.val,")")
        else:
            print(-1, ")")
        temp=temp.next
def copylinklist(head1):
    temp=head1
    dummmy=Node(-1)
    prev=dummmy
    while temp!=None:
        prev.next = Node(temp.val)
        prev = prev.next
        temp=temp.next
    return dummmy.next
def copyRandomlist(head1):
    if head1==None:
        return None
    head2=copylinklist(head1)
    t1=head1
    t2=head2
    while t1!=None and t2!=None:
        n1=t1.next
        n2=t2.next
        t1.next=t2
        t2.next=n1
        t1=n1
        t2=n2
    # set random pointer
    t1 = head1
    while t1 != None:
        if t1.random == None:
            t1.next.random = None
        else:
            t1.next.random = t1.random.next
        t1 = t1.next.next
    # Regain original list
    t1 = head1
    t2 = head2
    while t1!=None and t2!=None:
        n1=t2.next
        if n1==None:
            n2=None
        else:
            n2=n1.next
        t1.next=n1
        t2.next=n2
        t1=n1
        t2=n2
    return head2

def fun():
    listnode=[]
    prev=None
    n=int(input("enter number of nodes"))
    for i in range(n):
        listnode.append(Node(0))
        if prev!=None:
            prev.next=listnode[i]
        prev=listnode[i]
    for i in range(n):
        val=input("enter value ")
        idx=int(input("enter random index "))
        listnode[i].val=val
        if idx!=-1:
            listnode[i].random=listnode[idx]
    display(listnode[0])
    head=copyRandomlist(listnode[0])
    display(head)
fun()

def copyRandomlist1(head1):
    if head1==None:
        return None
    head2 = copylinklist(head1)
    #make linklist with next pointer only
    pointer_map={}
    #make a hashmap of node vs node and store original as key and clonned as value
    t1 = head1
    t2 = head2
    while t1!=None:
        pointer_map[t1]=t2
        t1=t1.next
        t2=t2.next
    for original_node in pointer_map.keys():
        #clonned node
        clonned_node=pointer_map[original_node]
        #original random node
        ori_rand_node=original_node.random
        if ori_rand_node==None:
            clonned_node.random=None
        else:
            clonned_node.random=pointer_map[ori_rand_node]

    return head2
class Node:
    def __init__(self, data=0,next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self,head=None,tail=None,size=0):
        self.head=head
        self.tail=tail
        self.size=size

    def addFirst(self,val):
        if self.size==0:
            nn=Node(val)
            self.head=nn
            self.tail=nn
            self.size += 1
        else:
            nn=Node(val)
            nn.next=self.head
            self.size+=1
            self.head=nn
def partition_index(ll,head,tail,pivot):
    i=head
    j=head
    while i !=tail:
        if i.data<=pivot:
            i.data,j.data=j.data,i.data
            i=i.next
            j=j.next
        else:
            i=i.next
    return j-1
def quicksort(ll,head, tail):
    if head == tail:
        return
    prev,pivot = partition_index(ll, ll.head, ll.tail, ll.tail.data)
    quicksort(ll, ll.head, prev)
    quicksort(ll, pivot.next, ll.tail)
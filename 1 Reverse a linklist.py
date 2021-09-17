class Node:
    def __init__(self, data=0,next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self,head=None):
        self.head=head

    def addFirst(self,val):
        if self.size==0:
            nn=Node(val)
            self.head=nn
        else:
            nn=Node(val)
            nn.next=self.head
            self.head=nn

    def reverse_linklist(self,node):
        prev=None
        cur=node
        while cur!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        self.head=prev

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
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def nth_position(self,node, pos):
        i = 0
        temp = node
        while i < pos - 1:
            if temp == None:
                return -1
            temp = temp.next
            i += 1
        return temp


    def reverse_ll(self,head, m, n):
        node1 = self.nth_position(head, m)
        if node1 == -1:
            return -1
        node2 = self.nth_position(head, n)
        if node2 == -1:
            return -1
        prev_node1 = self.nth_position(head, m - 1)
        next_node2 = node2.next
        temp_node1 = node1
        pre = node1
        cur = node1.next
        while cur != next_node2:
            temp = cur.next
            cur.next=pre
            pre = cur
            cur = temp
        prev_node1.next=pre
        temp_node1.next = next_node2
        return 1

ll=LinkList()
ll.addFirst(10)
ll.addFirst(20)
ll.addFirst(30)
ll.addFirst(40)
ll.addFirst(50)
ll.addFirst(60)
ll.addFirst(70)
ll.addFirst(80)
ll.display()
res=ll.reverse_ll(ll.head,3,6)
if res!=-1:
    ll.display()
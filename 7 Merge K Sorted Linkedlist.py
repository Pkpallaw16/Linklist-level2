import heapq
class pair:
    def __init__(self,node):
        self.node=node
    def __lt__(self, other):
        return self.node.val<self.node.val
def Merge_K_Sorted_Linkedlist(node_list):
    if len(node_list)==0:
        return None
    st=[]
    for i in range(len(node_list)):
        if len(node_list[i])>0:
            heapq.heappush(st,pair(node_list[i]))
    head=Node(-1)
    temp=head
    while len(st)>0:
        rem=heapq.heappop(st)
        temp.next=rem.node
        temp=temp.next
        if rem.node.next!=None:
            heapq.heappush(st,pair(rem.node.next))
    return head.next
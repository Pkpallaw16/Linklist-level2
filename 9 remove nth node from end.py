def remove_nth_node_from_end(node,n):
    slow = node
    fast = node
    pos = n
    while pos > 0:
        fast = fast.next
        pos -= 1
    if fast == None:
        return node.next
    while fast.next != None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return node

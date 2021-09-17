def middle_of_linlist(node):
    if node == None:
        return -1
    slow = node
    fast = node
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow.data
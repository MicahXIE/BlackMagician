'''
Delete A Node
https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

'''

def deleteNode(head, position):
    if not head:
        return head
    
    if position == 0:
        return head.next
    elif position > 0:
        prevPos = position-1
        tmpNode = head
        while (prevPos and tmpNode):
            prevPos -= 1
            tmpNode = tmpNode.next
        
        if (prevPos == 0) and tmpNode and tmpNode.next:
            tmpNode.next = tmpNode.next.next
            return head
        else:
            return head
    else:
        return head


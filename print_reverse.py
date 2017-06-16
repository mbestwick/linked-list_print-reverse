"""
You are given the pointer to the head node of a linked list and you need to
print all its elements in reverse order from tail to head, one element per line.
The head pointer may be null meaning that the list is empty - in that case, do
not print anything!

Input Format
You have to complete the void ReversePrint(Node* head) method which takes one
argument - the head of the linked list. You should NOT read any input from
stdin/console.

Output Format
Print the elements of the linked list in reverse order to stdout/console (using
printf or cout) , one per line.

"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def ReversePrint(head):
    stack = []
    curr = head
    while curr:
        stack.append(curr.data)
        curr = curr.next

    while stack:
        print stack.pop()

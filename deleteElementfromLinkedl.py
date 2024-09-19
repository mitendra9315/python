class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def createList(self,arr):
        self.head = None
        for i in range(len(arr)):
            node=Node(arr[i])
            if self.head is None:
                self.head=node
                self.start=self.head
            else:
                self.head.next=node
                self.head=node 
        return self.start
    def list_print(self,head):
        while head:
            print(head.val,end=" ")
            head=head.next
def main():
    arr=[8,6,1,8,6,5]
    ll= LinkedList()
    point=ll.createList(arr)
    ll.list_print(point)
main()




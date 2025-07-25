class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        self.prev=None

class Doublilinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertAthead(self,data):
        temp=Node(data)
        if not self.head:
            self.head=temp
        else:
            temp.next=self.head
            self.head.prev=temp
            self.head=temp

    def insertAttail(self,data):
        temp=Node(data)
        if not self.head:
            self.head=temp
        curr=self.head
        while(curr.next):
            curr=curr.next
        self.tail=curr
        self.tail.next=temp
        temp.prev=self.tail
        self.tail=temp

    def deletion(self,index):
        curr=self.head
        if index==1:
            self.head=self.head.next
            curr.next.prev=None
            curr.next=None
            del curr

        else:
            i=1
            while(i!=index):
              curr=curr.next
              i=i+1
            if curr==self.tail:
                self.tail=self.tail.prev
                curr.prev.next=None
                curr.prev=None
                del curr
            else:
                curr.prev.next=curr.next
                curr.next.prev=curr.prev
                curr.next=None
                curr.prev=None
                del curr



    def traversal(self):
        curr=self.head
        
        while(curr):
            print(curr.val,end="<->")
            curr=curr.next
        print("None")





FDlist=Doublilinkedlist()

FDlist.insertAthead(5)
FDlist.insertAthead(6)
FDlist.insertAthead(7)
FDlist.insertAttail(8)
FDlist.insertAttail(9)
FDlist.insertAttail(10)

FDlist.traversal()

FDlist.deletion(6)
FDlist.deletion(1)
FDlist.deletion(3)
FDlist.traversal()
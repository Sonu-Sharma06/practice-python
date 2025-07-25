
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


    def insert_head(self,head,val):
        temp=Node(val)
        if head==None:
            head=temp
        else:
            temp.next=head
           
        return temp
        
    
    def insert_tail(self,tail,val):
        temp=Node(val)
        tail.next=temp
        tail=temp
        return tail

def traverse(head):
    temp=head
    while temp:
        print(temp.data,end="-> ")
        temp=temp.next
    print("None")


node=Node(None)

head=None


head=node.insert_head(head,7)
tail=head

head=node.insert_head(head,6)

head=node.insert_head(head,3)


tail=node.insert_tail(tail,9)

tail=node.insert_tail(tail,3)

traverse(head)





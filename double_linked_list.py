import sys, os,pdb

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next =None
        self.prev =None

    def setData(self, data):
        self.data = data
        
    def setNext(self, next):
        self.next = next
        
    def setPrev(self, prev):
        self.prev = prev
        
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

class double_Linkedlist:
    def __init__(self):
        self.head = None
        self.tail =None

    def insertBegin(self, data):
        curr = self.head
        newnode = Node(data, None,None)
        if self.head == None:
            self.head = newnode
            self.tail =self.head
        else:
            newnode.setNext(self.head)
            newnode.setPrev(None)
            self.head.setPrev(newnode)
            self.head = newnode

    def insertEnd(self,data):
        curr = self.head
        newnode = Node(data,None,None)
        if self.head == None:
            self.head = newnode
            self.tail = self.head
        else:
            while curr.next !=None:
                curr=curr.next
            newnode.prev = curr
            curr.next = newnode
            self.tail= newnode

    def insertPos(self,pos,data):
        curr = self.head
        count = 1
        newnode = Node(data,None,None)
        if pos < 0 or pos >(self.getlength()):
            print "this position does not exist:"
            sys.exit(2)
        if pos == 0:
            newnode.next= self.head
            self.head = newnode
        elif pos ==(self.getlength()):
            while curr.next !=None:
                curr = curr.next
            newnode.prev = curr
            curr.next = newnode
            self.tail = newnode
        else:
            while count < pos:
                print count
                print curr.data
                curr = curr.next
                count += 1
            print "curr.data = {}".format(curr.data)
            newnode.next = curr.next
            print "newnode.next.data = {}".format(newnode.next.data)
            curr.next = newnode
            #print "curr.next.prev.data = {}".format(curr.next.prev.data)
            newnode.prev = curr
            newnode.next.prev =newnode 
            print "newnode.prev = {}".format(newnode.prev.data)
                
    def deleteAtPos(self, pos):
        len1 = self.getlength()
        curr = self.head
        prev =self.head
        count = 1
        if len1 == 0:
            print"Nothing to be deleted"
        if pos < 1 or pos > len1:
            print"Position does not exist.Error"
            sys.exit(2)

        if pos == 1:
            self.head = self.head.next
            self.head.prev = None
            
        elif pos == len1:
            while curr.next !=None:
                prev = curr
                curr=curr.next
            prev.next =None
            
        else:
            while count < pos:
                prev = curr
                curr=curr.next
                count =count + 1
            prev.next =curr.next
            curr.next.prev=prev

            
        
    def getlength(self):
        curr = self.head
        count = 1 
        while curr !=None:
            count = count + 1
            curr = curr.next
        print count 
        return (count-1 )

    def print_list(self):
        curr = self.head
        list1 = [] 
        while curr !=None:
            list1.append(curr.data)
            curr = curr.next 
        print list1

    def rev_pri(self):
        curr=self.head
        while curr!=None:
            prev = curr
            curr=curr.next
        while prev!=curr:
            print prev.data
            prev = prev.prev

    def getnode(self,pos):
        curr =self.head
        count = 1
        if pos < 1 or pos > self.getlength():
            print"This position does not exist"
            sys.exit(2)
            
        if pos == 1:
            print"node {} at position 1 is returned".format(self.head.data)
            return self.head
        else:
            while count < pos:
                curr = curr.next
                count = count + 1
            print "node {} at position {} has been returned".format(curr.data, pos)
            return curr
            

ob = double_Linkedlist()
ob.insertBegin(10)
ob.insertBegin(20)
ob.insertBegin(30)
ob.insertEnd(40)
ob.insertEnd(50)
ob.insertBegin(20)
ob.print_list()
ob.insertPos(6,100)
ob.print_list()
print"reverse"
ob.rev_pri()
print"Before"
ob.deleteAtPos(3)
ob.print_list()
ob.getnode(1)
ob.getnode(2)
ob.getnode(7)
            
            
            
        
        
 
    
    
   



        

        

        
        
                
            
            
        

        

        
      


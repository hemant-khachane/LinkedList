class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None

    def addnode(self,data):
        curr = self.head
        newnode = Node(data)
        if self.head == None:
            newnode.next = None
            self.head = newnode
        else:
            while curr.next !=None:
                curr = curr.next
            curr.next = newnode
            newnode.next = None

    def print_list(self):
        list1 = []
        curr = self.head
        while curr:
            list1.append(curr.data)
            curr = curr.next
        print list1

    def rev(self):
        curr = self.head
        prev = None
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def rec1(self):
        start = self.head
        self.rec_rev(self.head)
    
# Here is simple way of recursion. if we are asked to reverse string using recusrion. we can do it apply base condition like  reverse of single character is chracter itself. and
#same is applicable for linked list. like we can say that if nodes next if None we will return node to earlier recursive call and set pointer 
#def reversestring(s1):
##    if len(s1) == 1:
#      return s1[0]
 #   else:
 #       return reversestring(s1[1:]) + s1[0]

#print reversestring("abcd")
    


#Trivial/base condition for reversing single link list is
 # If node of next is None, return the node itself. If there is only single node
 # reverse of one node is node itself. Reverse of multi node is reverse of 
    def rec_rev(self,start):
        
        if start.next == None:
            self.head = start
            print"rec_rev"
            return start
        else:
            self.rec_rev(start.next)
            curr = start.next
            curr.next = start
            #start.next.next = start  # if we do not want to use earlier 2 statment, u can use start.next.next =start 
            start.next = None

    def insert_sorted(self,data):
        newnode = Node(data)
        curr = self.head
        prev = self.head
        found = 0
        # If new node to be inserted is 1st node 
        
        if self.head.data > newnode.data:
            newnode.next = self.head
            self.head = newnode
        else: 
            while curr and not found:   # if node is in between 1 st and last node 
                           
                if newnode.data < curr.data:
                    prev.next = newnode
                    newnode.next = curr
                    found = 1 
                else:
                    prev = curr
                    curr = curr.next
            if found == 0 and prev.data < newnode.data:  # if node to be inserted is last node
                prev.next = newnode
                newnode.next = None
        
    def lastN(self,k):
        tmp = self.head
        curr = self.head
        count = 1
        if k == 0:
            print "Enter correct position which start from 1"
            return False 
        while count <= k and curr!= None:
            curr = curr.next
            count = count + 1

        if count <= k:
            print "failed"
            return False

        while curr != None:
            curr = curr.next
            tmp = tmp.next

        print" %d th node from end of list is %d" %(k, tmp.data)

        
                


        
                
                
                
            
        
ll=Linked_list()
ll.addnode(10)
ll.addnode(20)
ll.addnode(30)
ll.addnode(40)
ll.addnode(50)
ll.print_list()
ll.addnode(100)
ll.print_list()
ll.rev()
ll.print_list()
ll.rec1()
ll.print_list()
ll.insert_sorted(1010)
ll.print_list()
ll.lastN(1)
ll.lastN(0)
ll.lastN(7)


            






























            
                

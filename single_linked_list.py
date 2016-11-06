import sys, os,pdb

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def setdata(self,data):
        self.data = data

    def setnext(self, next):
        self.next = next

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def hasnext(self):
        return self.next != None

    
class linked_list(object):

    def __init__(self):
        self.length = 0
        self.head = None

    def addnodes(self,node):
        current = self.head
        newnode = node
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addEnd(node)
        

    def addBeg(self, node):
        print"Inside addBeg"
        if self.length == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def addEnd(self, node):
        print"Inside addEed"
        curr = self.head
        newnode     = node
        while curr.next != None:
            curr = curr.next
        curr.next = newnode
            
        self.length += 1
               
    
    def Mid(self, pos, node):
        curr = self.head
        count = 1 # Start from count =1 first node is 0th position but counted as 1st node 
        newnode = node
        #print pos
        #print self.length
        self.length = self.len1()
        if self.length == 0:
            print"Empty link list ...form the link list first"
        if pos < 1 or pos >(self.length+1) :
            print" Error, position {} does not exist".format(pos)
            return sys.exit(2)
        if  pos == 1:  # we assume that position is 1 means we add node at 1st postion or 1st element 
            newnode.next = self.head
            self.head = newnode
            self.length += 1 
        elif pos == (self.length + 1): # if lenght is say n, so pos  is lenght+1 so start from 1 to n  and add elements  
            # As we know that we are starting with curr and cheking for curr.next so when last nodes next become Null last node is pointed by Curr.
            while curr.next != None:
                curr = curr.next
            newnode.next = None # may not be required as while creating new node we are setting it to None
            curr.next = newnode
            self.length += 1 
        else:
            # I always follow that insert node at nth position means start from 1 and visit till n-1 node.Once we reach here, insert new element at nth place
            while count < (pos-1):
                curr = curr.next # when count =1 curr become next so 2 so when count =pos-1 curr goes to pos element whereas we need to stop at position-1
                count = count + 1
                print count
                #print curr
            newnode.next = curr.next
            curr.next = newnode
            self.length += 1 


    def insertAfterVal(self,data,node):
        curr = self.head
        newnode = node 
        while curr.next !=None:
            if curr.data == data:
                break
            else:
                curr = curr.next
                
        if curr.data ==data:
            newnode.next = curr.next
            curr.next = newnode
        else:
            print"data did not found:"
            
       

    def Del(self, pos):
        curr = self.head
        prev = self.head 
        count = 1
        length1 = self.len1()
        print length1
        
        if pos < 1 or pos >length1:
            print"Error. position{} does not exist".format(pos)
            return 
        if pos == 1:
            self.head = self.head.next
            self.length -= 1
        elif pos == self.length:
            while curr.next !=None:
                prev = curr
                curr = curr.next
            prev.next = None
            curr = prev
            
        else:
             while count < pos:
                 prev = curr
                 curr = curr.next
                 count = count + 1 
             prev.next = curr.next
             curr = prev 
             self.length -= 1
   
    
    def AddAfterValue(self,data,node):
        curr = self.head
        newnode = node
        
        while curr.next != None:
            if curr.data == data:
                break
            else:
                curr = curr.next
            
        if curr.data == data:
            newnode.next = curr.next
            curr.next = newnode
           
        else:
             print "Valus does not match"

    def AddBeforeValue(self,data,node):
        curr = self.head
        prev = self.head
        newnode =node
        if self.head.data == data:
            newnode.next =self.head
            self.head = newnode
        else:
            while curr.next !=None:
                if curr.data == data:
                    break
                else:
                    prev =curr
                    curr =curr.next
                
            if curr.data == data:
                newnode.next=curr
                prev.next = newnode
            else:
                print"no data {}found".format(data)
                
        

    def DelAfterValue(self,data):
        curr = self.head
        while curr.next !=None:
            if curr.data == data:
                break
            else:
                curr = curr.next

        if curr.data == data:
            if curr.next !=None:
                curr.next = curr.next.next
                self.length -= 1
            else:
                print'There is no data after data {}'.format(data) 

    def getlength(self):
        count = 1
        curr = self.head
        while curr.next != None:
            curr = curr.next
            count = count + 1
        return count 
            
    def getdata(self,pos):
        count = 1
        curr = self.head
        if pos<0 or pos >self.length:
            print "position does not exist"
            return 
        while curr.next !=None and count < pos:
            count = count + 1 
            curr =curr.next
        if count == pos:
            return curr.data

    def len1(self):
        curr = self.head
        count = 1
        # Assume that list always start with index 1. If we declare count=1
        #and curr!=None then while visiting last Nth node, count will be N+1.So in end do -1
        # so  best way is say count =1 and curr!=None or count=0 and curr-Next!=None
        while(curr!=None):
         #   print"Count = {}, curr.data = {}".format(count, curr.data)
            curr = curr.next
            count = count + 1
        # As we have taken count=1 and curr!=Null so curr will be counted as 1 and when
        # it reaches to None, count will be counted as N+1 (additional 1 count)So reduce it in the end
        
        #print "count = {}".format(count-1)
        return (count-1)
        
            
    def print_list( self):
        list1 = [] 
        curr = self.head 
        while curr != None:
            #print curr.data
            list1.append(curr.data)
            curr = curr.next
        print list1
                
    def rev(self):
        curr = self.head
              
        last  = None
        while curr !=None:
            curr1 = curr.next   
            curr.next = last
            last = curr
            curr = curr1
        self.head = last
        
        
    def finN_fromend(self, n ):
        curr = self.head
        curr1 = self.head
        count = 1
        if n == 0:
            print" ERROR, Incorrect element,Index should start from 1 "
            sys.exit(2)
        

        while curr != None and count < n:
            curr =curr.next
            count = count + 1
           # print curr.data
        
        if count < n or curr == None:
            print"List length is less than {}".format(n)
            sys.exit(2)

        while curr.next!=None:
            curr1= curr1.next
            curr = curr.next
        print "Node {} from end is {}".format(n,curr1.data) 
        return curr1
    
    def find_fromEndbyVal(self, val):
        count = 1
        k = count
        curr=self.head
        tmp = None

        while curr!=None:
            if curr.data == val:
                k = count
                tmp = curr
            count = count + 1
            curr = curr.next
        print"The nearest Node having value of {} is at position {} from end of linked list".format(val,k)
        return k
# Here we are setting loop. 
    def add_loop(self):
        print"Inside add_loop"
        curr = self.head
        prev = self.head.next.next 
        while curr.next != None:
            curr = curr.next
        curr.next = prev   
        
# This will detect loop. This will take O(n^2)
    def detect_loop(self):
        list1 = []
        flag = 0 
        curr =self.head
        while curr !=None:
            if curr not in list1:
                list1.append(curr)
            else:
                flag = 1
                break 
            curr = curr.next
        if flag ==1:
            print "there is loop"
        else:
            print ":There is no Loop:"
        
# This will detect loop  in O(n)
    def detect_loop1(self):
        flag = 0
        curr = self.head
        curr1 = self.head.next
        while curr and curr1:
            if curr == curr1:
                flag =1
                break
            else:
                curr = curr.next
                curr1 = curr1.next.next
        if flag:
            print":There is Loop"
        else:

            print"there is no Loop"

# Always use this method O(n). User 2 pointers both pointing to same starting node of list.This is Floyds algorithm
#Move curr pointer by one position whileas move curr1 pointer by 2 positions. There will be time when they meet at some node. May not be the same node where loop started.

    def loop(self):
        flag =0 
        curr = curr1 = self.head    
        while (curr and curr1 and curr1.next):
            curr = curr.next
            curr1 = curr1.next.next
            if curr == curr1:
                flag = 1 
                print "Loop is detected"
                break
        if not flag :
            print "No Loop"
# For finding out node where loops starts, use method like reach to point where you detect loop. keep curr1 pointer which is moving faster at same place. Set Slow pointer Curr to self.head
# and start incrementing both pointers only by one position. and it will exactly meet at the point where loops starts.
# M is distance starting from 1st node to node where loop starts, l is total loop length, K is node where both slow and fast pointers meets. so
# distance travelled by slow poniter is D_curr = K + M + p*l( one may have to go through loop couple of times )
# fast pointers moves with double speed  so D_curr1 = K + K + q*l = 2(D_curr) ~=> (M+K) = (q-2p)l = M+K is integer multiple of lenght of loop. 
    def first_node_loop(self):
        flag = 0 
        curr = curr1 = self.head
        while (curr and curr1 and curr1.next):
            curr = curr.next
            curr1 = curr1.next.next
            if curr == curr1:
                flag = 1
                break
        curr = self.head
        while curr!=curr1:
            curr = curr.next
            curr1 = curr1.next
        print" first node where loop start is curr {} having data = {}".format(curr, curr.data)
        
                
# Find lenght of loop.
    def len_loop(self):
        curr = curr1 = self.head
        count = 0
        flag = 0
        while(curr and curr1 and curr1.next):
            curr = curr.next
            curr1 = curr1.next.next
            if curr == curr1:
                flag = 1
                break
        if flag == 1:
            while curr.next!=curr1:
                count = count + 1 # count we starting from 0 because both curr and curr1 points to same, when curr become curr.next then only count will be 1. In end when curr.next==curr1, count will not be incremented. 
                curr = curr.next
            print "length of loop is {}".format(count)
        else:
             print'No loop Detected'
    def rec1(self):
        self.recursion_rev(self.head)
   
    def recursion_rev(self,curr):
        if  None !=curr:
            right = curr.next
            if self.head !=curr:
                curr.nexr = self.head
                self.head = curr
            else:
                curr.next = None
            self.recursion_rev(right)

    def recursiveReverseList(self):
        self.reverseRecursive(self.head)
    def reverseRecursive(self, n):
        if None != n:
            right = n.getnext()
            if self.head != n:
                n.setnext(self.head)
                self.head = n
            else:
                n.setnext(None)
            self.reverseRecursive(right)
           
ob1 = Node(10)
ob2  = Node(20)
ob3 = Node(30)
ob4 = Node(40)
ob5 = Node(50)
ob6 = Node(60)
ob7 = Node(70)
ob8 =Node(80)
ob9 = Node(10)
ob10 = Node(10)
ll = linked_list()
ll.addnodes(ob1)

print "All elements are added"
ll.print_list()

print "Add element at 1"
ll.Mid(1,ob5)
ll.print_list()
print "Add element at 2"
ll.Mid(2,ob3)
ll.print_list()
#print "Add element at 2"
#ll.Mid(2,ob7)
#ll.print_list()
print "Add element at 4 "
ll.Mid(4,ob6)
ll.print_list()
ll.AddBeforeValue(60,ob7)
ll.print_list()
print "Add element at 80 after 10 "
ll.insertAfterVal(30,ob8)
ll.print_list()
ll.Del(2)
ll.print_list()
ll.finN_fromend(1)
ll.print_list()
ll.AddAfterValue(80,ob9)
ll.Mid(2,ob10)
ll.print_list()
ll.find_fromEndbyVal(10)
ll.add_loop()
#ll.detect_loop()
#ll.detect_loop1()
#ll.detect_loop()
#ll.first_node_loop()
#ll.len_loop()
curr = ll.head
#ll.rec1()
#ll.recursiveReverseList()
#ll.print_list()


        

        

        
        
                
            
            
        

        

        
      


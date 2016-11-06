import sys,os,random,pdb
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_list:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def insert(self, data):
        curr = self.head
        newnode = Node(data)
        newnode.next = newnode 
        if self.head == None:
            self.head = newnode
        else:
            while curr.next!=self.head:
                curr = curr.next
            curr.next = newnode
            newnode.next = self.head
            self.tail = newnode
            print newnode.data

    def delete_node_atvalue(self,val):
        curr = self.head
        prev = self.head

        if self.head == None:
            print "Circular link list is empty"
            sys.exit(2)

        if self.head.next == self.head:
            print"Last node is deleted from circular link list"
            
            
            
        while curr.next != self.head: #this is to find last node of list whihc is pointing to head
            prev = curr   
            curr  = curr.next
        # Here we have not maintained tail if we remove comments. If we need to maintain tail pointer we will use below logic
        if self.head.data == val:
            curr.next = self.head.next
            self.head = self.head.next
            
        elif curr.data == val:
            prev.next = self.head
            
            
        else:
            prev = curr = self.head 
            while curr.next !=self.head:
                if curr.data == val:
                    prev.next = curr.next
                    break 
                prev = curr 
                curr = curr.next
                     
               
       

    def print_circular_linkedList(self):
        curr = self.head
        list1 = []
        list2 = [] 
        if self.head == None:
            return 0
                  
        list1.append(curr.data)   
        curr = curr.next
        
        while curr!=self.head:
            list1.append(curr.data)
            curr = curr.next
        print list1

      #  while curr!= self.tail :
      #      list2.append(curr.data)
      #      curr = curr.next
       # print list2
    
        

    def count_nodes(self):
        curr = self.head
        count = 1
        while curr.next!= self.head:
            count = count + 1
            curr = curr.next
        print "Total nodes in circular link list is {}".format(count)
        return count

ll = Circular_list()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.print_circular_linkedList()
ll.count_nodes()
print "delete at 10"
ll.delete_node_atvalue(10)
ll.print_circular_linkedList()
print "delete at 40"
ll.delete_node_atvalue(40)
ll.print_circular_linkedList()
print "delete at 20"
ll.delete_node_atvalue(20)
ll.print_circular_linkedList()

print "delete at 30"
ll.delete_node_atvalue(30)
ll.print_circular_linkedList()

            

            
        
            
            
            
            
    

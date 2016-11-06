class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Que:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        

    def enque(self, data):
        tmp = Node(data)
        if self.front==None and self.rear ==None:
            self.front = tmp
            self.rear=tmp
            self.size += 1
            return
        else:
             
            self.rear.next = tmp
            self.rear = tmp
            self.size += 1

    def deque(self):
        if self.front ==None:
            print"Queue is empty"
            return
        
        if self.front ==self.rear :
            self.front=self.front=None
            print"Queue is empty"
        else:
            self.front = self.front.next
            self.size -=1

    def queFront(self):
        if self.front!=None:
            print"Node is {}".format(self.front.data)
            return self.front

    def ssize(self):
        return self.size

    def pri(self):
        k = []
        tmp = self.front
        if self.front == self.rear:
            print "empty"
            return None
        
        while tmp:
            k.append(tmp.data)
            tmp =tmp.next
        print k 
            


ob = Que()
for i in range(0,10):
    ob.enque(i)

ob.pri()

for i in range(0,9):
    ob.deque()
    ob.pri()
ob.enque(500)
#ob.enque(1000)
print "hi"
ob.pri()



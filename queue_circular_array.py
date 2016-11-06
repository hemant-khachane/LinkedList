class que_arr:
    def __init__(self, limit=10):
        self.limit =limit
        self.que = [None]*limit
        self.front = -1
        self.rear = -1
        self.size = 0
        
    def isEmpty(self):
        return self.front == self.rear == -1
             

    def enque(self, data):
        #if self.size >=self.limit:
         #   print"Queue is Full"
        #    return

        if ((self.rear+1)%self.limit) == self.front:
            print"Queue is Full:"
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            #self.rear = self.rear + 1
            self.rear = (self.rear +1)%self.limit

        self.que[self.rear] = data
        #print self.que
        #print self.rear

    def deque(self):
        if self.isEmpty():
            print"Queue is empty"
            return
        if self.front ==self.rear:
            self.front= self.rear = -1
        else:
            self.front=(self.front+1)%self.limit

    def pri(self):
        k = []
        tmp =self.front
        count = (self.rear+self.limit-self.front)%self.limit + 1
        for i in range(count):
            index = (self.front+i)%self.limit
            k.append(self.que[index])
        print k
        

ob = que_arr()
for i in range(0,10):
    ob.enque(i*10)
ob.pri()
#print ob.que
for i in range(0,2):
    ob.deque()
#print ob.que
ob.pri()
ob.enque(10)
ob.enque(11)
#print ob.que
ob.pri()


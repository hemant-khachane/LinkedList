import sys, os,random
from stack_using_list import Stack

s2 = Stack()
s2.print_stack()
list1 = []
def balenced1(s1):
    
    balenced = 0
    s2 = Stack() 
    for i in s1:
        if i in ["({[:
            print i
            s2.push(i)
            
        else:
            if s2.isstackempty():
                balenced = 1
                
            else:
                top = s2.pop()
                
                print i
                print top
                if not matchs(top, i):
                    balenced = 0
                else:
                    balenced =1 
                    
    if balenced:
        print"Balenced"

def matchs(op1, op2):
    t1 ="({["
    t2 = ")}]"

    return t1.index(op1) == t2.index(op2)
    





balenced1("{{([][])}()}")

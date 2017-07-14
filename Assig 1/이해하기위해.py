#So, nodes must, MUST CONTAINT THE REFERNCE TO THE NEXT NODE
#ALSO, THE CARGO(OR WHATEVER, DATA MAY IT BE CALLED) THAT HOLDS THE DATA THAT USER WANTS!
#Also, it NEEDS to have the capability to RETURN A DATA THAT HAS.
#알았습뉘꺄?
class Node:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

    def get_data(self):
        return self.data

#큰일이네요..
#First, if the LinkedList does not have a head, then it becomes a pointless data.
#The reason is because...
#SEARCHING
#ADDING
#CHECKING THE SIZE
#EVERYTHING starts with the head.
class LinkedList:

    def __init__(self):
        self.head = None
#왜냐? 어차피, head로부터 LinkedList의활용이 시작됀다.
#이유는, Node마다, 다음(next)에있는 Node들이 연결돼어있으니깐.
#head부터 Node들이 이어지는데, 거기가비어있으면,
#비어있다는의미다?
    def is_empty(self):
        return self.head == None

#Please add this to the linked list
#That's the case with the abstract sense.
#으어어
#So, the philosophy is that
#I need to have the material in the head pushed to next,
#and have current material take over the assigned to head.
    def add(self, item):
        

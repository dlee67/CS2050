#이거 git hub에서 훔쳐온거니깐,
#reference 않하면 교수님이 화날수도있으니깐,
#이 코드같고 점수까질려면 어떻게해야돼냐고
#여쭤봐야겠다.


#아직도이것이 리스트(어레이 리스트든)
#처럼 사용됄수있다는게 믿기지가않아...!
class LinkedList:

    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
#처음에 리스트에 아무것도없으면
#거기안에 데이타가박히는데.
#리스트가 뭘소지하고있느와중
#이프로그램은 그데이타를 "밀어버린다고 할수도있나?"
#"next" field가 전데이타를 소지하게돼.

#알겠다, Node가 next를 소지하고있기에 가능해
#이거어떤사람이 만든거지

    def empty(self):
        
        return self.head == self.tail == None
        
    def add(self, data):
        new = self.Node(data, self.head)
#The start of the very last Node
#
#The innitialization of the very last node is here.
#
#왜? Why?
#
#As the method has implied in as the "abstract data type",
#
#the linked data is imitating the "pushing" action in literal life.
#
#That means, the very first Node is PUSHED TO THE VERY END 
#
#EACH TIME A NEW NODE IS BEING ADDED.
#
#무슨뜻이지? What does that mean?
#
#the tail of the linked list is referencing the end of the linked list
#
#since the beginning of the establishment of the linked list.
#
#그러면 이렇게말해도됀다. "링크드이스트는 다이나믹이아니라 우선위주로이용돼는 프로그램이다."
#
#Then I can sum it up as this,
#
#   "Linked List is not dynamic, it is heavily procedural."
#
#ta da
#
#천재다, 나였다면, 이런생각, 날수도있게지만, 이런생각나면 그건 하느님이 나에세 기회같은걸 준거나
#마찬가지다.
#
#
#Brilliant.
#
#
#
#
        if self.empty():
            self.head = self.tail = new
        #저위에있는 코맨트는 여기가 증명하고있다!!!!!    
        else:
            self.head = new

    def add_tail(self, data):

#Got an error over here that the computer is telling me
#"I can't  have new assigned with None.
#So, I wrote self

#       newer = self.Node(data, None)

        old = self.tail

        new = self.Node(data, None)

        if self.empty():
            
            self.add(new)
            
        else:
#If the statement below is working...
#Then how is tail seating at the end of the linked list?
#Thing is suppose to point to nothing
#However, if the statement below is truely being included in the
#linked list, then that statement below is the
#
#   "last node of the linked list"
#
#I think,
#
#   then how?
#
            old.next = new

            self.tail = old
            
#Now, I have the computer telling me
#"Inside the linked list, there is no such thing as new.
#then, I erased self, and typed in new
#Now, it's telling me, next is noneType, there is nothing there.
#Computer is right, tail's next is None.
#솔직히 더망가트린겄같다.

    #def remove(self, item): #The thing is that Dr. Beatty mentioned about
                            #something called garbage collector and I do not need to
                            #create a method that specifically removes the node.

    def __str__(self):
        s = ""
        p = self.head

        if p != None:
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data

        return s

linked = LinkedList()

linked.add('3')
linked.add('2')
linked.add('1')
#Despite all the invokations for the add_tail
#the linked list does not grow whatsoever.
#The tail is really seating over there in the console, alone.
#3217 is the out, there is not 4 5 6
#
#
#노오오오오오오오오오오오오오오오오오오오오오오오오력
#여길보시오
#
#Q:
#I don't even understand how the tail is even a part of a linked list,
#taking a consideration that I didn't try to link the last node of the
#linked list to the tail
#
#
#
#
#
linked.add_tail('4')
linked.add_tail('5')

#근데왜 우선순위가 거꾸로지....?
print(linked)

class Node:

#In full obviousness, data holds the value that I want to store at a specific node.
#next "points" to the next node.
#
#
#
#
#
#
#
#
#
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_Next(self):
        return self.next

    def setItem(self, item):
        self.item = item

    def set_Next(self, otherside):
        self.next = otherside

    def __str__(self):

        str1 = str(self.data)

        str2 = str(self.next)

        return str1 + " " + str2

#Is the sole purpose of the get_next is to get the "next" of the
#"current" node?
#If that is the case, is it ultimately useless to have the get_next
#invoked outside of the LinkedList(in my case, UnorderedList) class?
    def get_next(self):
        return self.next

    def set_data(self, new_data):
        seld.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class UnorderedList:

    def __init__(self):
        self.head = None

        self.tail = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def addTail(self, item):
#일딴Node는 많들어놨어요.
#근데, 이게끝부분부터 이어져야하는데.
        temp = Node(item)
        temp.set_next(self.tail)
        self.tail = temp
        
        

    def size(self):
        current = self.head
        count = 0
        while current != None:
            #물론, Node가있을때마다
            #count는 올라가고.
            count = count + 1
            #여기서는 next가소지하고 있는 Node를같고온다.
            current = current.get_next()

        return count
#그런데, if I am trying to find a specific node,
#I need to have a method similar to below.
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
#So, the statement below is suppose to kill the loop.
#I am guessing because the above condition is now false
#and the loop terminates.
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

#In order to remove the item, I need to modify the previous node
#so that it refers to the node that comes after.
#STOPPED AT PAGE 105
#In order to remove the node, I must actually have two nodes 
#scanning through the list.
#One of the two will behave like a usual search
#the other one will behave in a manner that it's always node behind.
#Meaning, when the current node finds the node to be removed,
#the node behind will get rid of the node the current found,
#with the assignment None.

#님마, 여기주목하셈,
#7:12PM 05/30/2016
#The item that I am looking for most likely be not the first node;
#therefore, else block will be ran into and previous will become the head,
#and current will be the "next" of the previous node.
#So, on the second else block, previous will have its next set as the
#current's next. What does that mean?
#I am squeezing things together in a sense.
#If my item is the first node of the LinkedList,
#then I get the "next" of the head in the LinkedList,
#and set that thing as the head itself.
#Again, I am squeezing things.
#그래도, str같은 method을사용해서, 어떻게 구조가진행돼는지보자.
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

#It repeats alright, but doesn't stop....
#Now it stops but still having trouble annalyzing what is going on.
#여기보세요, 보아버지하고 철수아버지의 엠에스엔. 7:15PM 05/31/2016
    def __iter__(self):

        wheel = self.head

        while wheel is not None:

            yield wheel.data

            print(wheel)

#님마즐!!! 암튼, 여기 주목,
#append를왜우기위해선, 여길주목
#근데, 책에서는 않가르쳐주는군요...
#큰일이에요...
#pg 107에멈춤.
                    
linked = UnorderedList()

linked.add(3)
linked.add(2)
linked.add(1)
linked.search(3)
print(linked.search(2))
print(linked.__iter__())
#노오오오오오력해도 않됐어요...
#below statement.
#linked.__iter__()

#왜 address에있는 어치를주는거지...?
#아... __str__ 이없구나
#toString같은거말야...

#아산에겐 젊음을바치세요, 나머지는, 우리가해겠습니다.

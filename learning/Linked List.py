# Node class
class Node:

	# Function to initialize the
	# node object
	def __init__(self, data):

		# Assign data
		self.data = data

		# Initialize next as null
		self.next = None

# Linked List class
class LinkedList:

	# Function to initialize the
	# Linked List object
    def __init__(self):
        self.head = None
    def insert_at_the_beginning(self, data):
        '''
        [data]->[5]->[8]->NULL
        '''
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def insert_at_the_end(self, data):
        '''
        [5]->[8]->[data]->NULL
        '''
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
    
    def get_length(self):
        '''
        return length
        '''
        count = 0
        iter = self.head
        while iter:
            iter = iter.next
            count += 1
        return count

    def delete_at_index(self, index):
        '''
        Before: [5]->[8]->[9]->NULL
        given index = 1
        After: [5]->[9]->NULL
        '''
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Exception')
        if index == 0:
            self.head = self.head.next
        
        count = 0
        iter = self.head
        while iter:
            if index - 1 == count:
                iter.next = iter.next.next
                break
            count += 1
            iter = iter.next
        return 

    def printList(self):
        temp = self.head
        comp = ''
        while (temp):
            comp += str(temp.data) + '->'
            # print(temp.data)
            temp = temp.next
        print(comp)




ll = LinkedList()
ll.insert_at_the_beginning(5)
ll.insert_at_the_beginning(50)
ll.insert_at_the_end(32)
ll.insert_at_the_beginning(43)
ll.insert_at_the_beginning(22)
ll.insert_at_the_end(11)
print(ll.get_length())
ll.printList()
ll.delete_at_index(2)
print(ll.get_length())
ll.printList()

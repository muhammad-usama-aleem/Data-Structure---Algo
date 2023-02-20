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
ll.printList()

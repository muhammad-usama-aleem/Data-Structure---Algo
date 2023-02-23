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

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Exception')
        if index == 0:
            self.insert_at_the_beginning(data)
            return
        
        count = 0
        iter = self.head
        while iter:
            if index-1 == count:
                node = Node(data)
                node.next = iter.next
                iter.next = node
                break
            iter = iter.next
            count += 1
        
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        count = 0
        iter = self.head
        while iter:
            if iter.data == data_after:
                node = Node(data_to_insert)
                node.next = iter.next
                iter.next = node
                break
            iter = iter.next
            count += 1
            

    
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
            return
        
        count = 0
        iter = self.head
        while iter:
            if index - 1 == count:
                iter.next = iter.next.next
                break
            count += 1
            iter = iter.next
        return 

    def remove_by_value(self, data):
        # Remove first node that contains data
        iter = self.head
        while iter:
            if iter.next.data == data:
                iter.next = iter.next.next
                break
            iter = iter.next



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
ll.insert_at_the_end(11)
print(ll.get_length())
ll.printList()
ll.delete_at_index(2)
print(ll.get_length())
ll.printList()
ll.insert_at_index(3, 78)
ll.printList()
ll.insert_after_value(11, 21)
ll.printList()
ll.remove_by_value(11)
ll.printList()
ll.remove_by_value(21)
ll.printList()

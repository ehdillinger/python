class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None
	
	def getData(self):
		return self.data
	
	def getNext(self):
		return self.next
	
	def setData(self):
		self.data = newdata
	
	def setNext(self, newnext):
		self.next = newnext
		
class linkedList:

	def __init__(self):
		self.head = None
	
	def isEmpty (self):
		return self.head == None
	
	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
	
	def size(self):
		current = self.head
		count = 0
		while current!= None:
			count = count + 1
			current = current.getNext()
		return count
	
	def search(self, item):
		current = self.head
		found = False
		while current != None and found != True:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found
			
	def delete(self, item):
		current = self.head
		previous = None
		found = False
		while current != None and not found:
			if current.getData()==item:
				found = True
			else:
				previous = current
				current= current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

myList = linkedList()
myList.add(23)
myList.add(13)
myList.add(3)
myList.add(99)
myList.add(12)
myList.add(18)
myList.add(67)
myList.add(55)
myList.add(43)


print myList.size()
print myList.search(26)

			
			
				

		
	

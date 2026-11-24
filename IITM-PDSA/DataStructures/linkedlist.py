class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = None

    def append(self, value):
        if self.value == None:
            self.value = value
        elif self.next == None:
            self.next = Node(value)
        else:
            self.next.append(value)

    def insert(self, value):
        if self.value == None:
            self.value = value
        else:
            new_node = Node(self.value)
            self.value = value
            new_node.next = self.next
            self.next = new_node

    def __str__(self):
        if self.value == None:
            return '[]'
        else:
            arr = []
            temp = self
            while(temp!=None):
                arr.append(temp.value)
                temp = temp.next
            return str(arr)

    def delete(self, value):
        if self.value == None:
            return
        if self.value == value:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if(self.next != None):
                self.next.delete(value)
                if self.next.value == None:
                    self.next = None


head = Node()
print(head)
head.append(10)
head.append(20)
head.append(30)
head.append(40)
print(head)
head.insert(10)
head.insert(20)
head.insert(30)
head.insert(40)
print(head)
head.delete(10)
head.delete(20)
head.delete(30)
head.delete(40)
head.delete(40)

print(head)
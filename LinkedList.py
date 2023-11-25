from Node import Node

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return new_node.value

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node.value

    def pop_last(self):
        if self.head == None:
            return None
        temp = self.head
        prev = self.head
        while temp.next != None:
            prev = temp
            temp = temp.next
        prev.next = None
        self.tail = prev
        self.length -= 1
        return temp.value

    def pop_first(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp.value

    def insert_at(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node.value
        elif index == 0:
            self.prepend(value)
        else:
            counter = 0
            temp = self.head
            prev = self.head
            while temp != None and counter != index:
                prev = temp
                temp = temp.next
                counter += 1
            new_node.next = temp
            prev.next = new_node
            self.length += 1
            return new_node.value

    def remove_at(self, index):
        if self.head == None or index >= self.length:
            return None
        elif index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop_last()
        else:
            counter = 0
            temp = self.head
            prev = self.head
            while temp != None and counter != index:
                prev = temp
                temp = temp.next
                counter += 1
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp.value
    
    def reverse_list(self):
        if self.head is None:
            return
        prev = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def search(self, val):
        if self.head == None:
            return None
        else:
            temp = self.head
            while temp != None:
                if temp.value == val:
                    return temp.value
                temp = temp.next
            return None
    
    def update_at(self, index, val):
        if self.head == None or index < 0 or index >= self.length:
            return None
        counter = 0
        temp = self.head
        while temp != None and counter != index:
            temp = temp.next
            counter += 1
        temp.value = val
        return temp.value
def destack_with_logging(func):
    def wrapper(self):
        print(f"Getting item... Current stack size: {self.length}")
        item = func(self)
        print(f"Got item: {item}. Updated stack size: {self.length}")
        return item
    return wrapper


# Build a custom `Stack` similar to the `Queue` you built
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class stack:
    def __init__(self, value = None):
        self.head = None
        self.tail = None
        self.length = 0
    
    def is_empty(self):
        return self.head is None
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value
        
    def stack_push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    @destack_with_logging
    def stack_pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            self.length -= 1
            if self.is_empty():
                self.tail = None
                return popped_node.value
            else:
                return popped_node.value
            






# Creat a new 'Stack' object
morning_tasks = stack()
morning_tasks.stack_push("get to work")
morning_tasks.stack_push("eat breakfast")
morning_tasks.stack_push("get dressed")

morning_tasks.peek() 


tasks = morning_tasks.stack_pop()
#print(tasks)
tasks = morning_tasks.stack_pop()
#print(tasks)
tasks = morning_tasks.stack_pop()
#print(tasks)

       
        
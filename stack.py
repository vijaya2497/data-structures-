
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    def print(self):
        tmp = self.top
        while(tmp):
            print(tmp.value)
            tmp = tmp.next
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = temp.next 
            temp.next = None
        self.height -= 1
        return temp
    def get_min_ele(self):
        min  = self.top.value
        temp = self.top
        while(temp):
            if temp.value < min:
                min = temp.value
            temp = temp.next
        return min
    def get_max_ele(self):
        max  = self.top.value
        temp = self.top
        while(temp):
            if temp.value > max:
                max = temp.value
            temp = temp.next
        return max



s = stack(3)
s.push(4)
#s.print()
print(s.get_max_ele())


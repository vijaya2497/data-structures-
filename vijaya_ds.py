


class Node:
      def __init__(self, value):
       self.value = value
       self.next = None

class LinkedList:
      def __init__(self, value):
          new_node = Node(value)
          self.head = new_node
          self.tail = new_node
          self.length = 1

      def  print(self):
          temp = self.head
          while (temp):
              print(temp.value)
              temp = temp.next
      def  append(self, value):
          new_node = Node(value)
          if self.length  == 0:
              self.head = new_node
              self.tail = new_node
          else:
              self.tail.next = new_node
              self.tail = new_node
          self.length += 1
      def  pop(self):
          if self.length == 0:
              return None
          temp = self.head
          pre = self.head
          while(temp.next):
              pre = temp
              temp = temp.next
          self.tail  = pre
          self.tail.next = None
          self.length -= 1
          if self.length == 0:
              self.head = None
              self.tail = None
          return temp.value
      def prepend(self, value):
          new_node = Nod(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                #new_node = Node(value)
                temp = self.head
                self.head = new_node
                new_node.next = temp
            self.length += 1
      def  pop_first(self):
         if self.length == 0:
             return None
         temp = self.head
         self.head = self.head.next
         temp.next = None
         self.length -= 1
         if self.length == 0:
             self.tail = None
         return temp.value

      def  get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

      def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
      def insert(self, index, value):
          if index < 0 or index > self.length:
              return False
          if index == 0:
             return  self.prepend(value)
          if index == self.length:
              return self.append(value)
          new_node =  Node(value)
          temp = self.get(index-1)

          new_node.next = temp.next
          temp.next = new_node
          self.length += 1
          return True
      def remove(self, index):
          if index < 0 or index > self.length:
              return False
          if index == 0:
             return  self.pop_first()
          if index == self.length:
              return self.pop()
          pre = self.get(index-1)
          temp = pre.next
          pre.next = temp.next
          temp.next = None
          self.length -= 1
          return temp
      def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
      def  middle(self):
          count = 0
          mid = self.head
          tmp = self.head
          while (tmp != None):
              if count & 1:
                  mid = mid.next
              count += 1
              tmp = tmp.next
          return mid.value
      def count(self, ele):
          count = 0
          tmp = self.head
          while(tmp):
              if tmp.value == ele:
                  count = count+1
              tmp =tmp.next

          return count
    
#def print_reverse(head):
    #if head == None:
        #return 
    #else:
        #print_reverse(head.next)
        #print(head.value)


  

          


         






      

        
l = LinkedList(6)   
l.append(3)
l.append(4)
#l.print()
#l.pop()
l.prepend(2)
l.prepend(3)
#l.pop_first()
#l.print()
#print(l.get(2))
#l.set(1,7)
#l.insert(1,2)
#l.remove(1)
#l.print()
#l.reverse()
#l.print()
#print_reverse(l.head)
#print(l.middle())
#print(l.count(3))



    
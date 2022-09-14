class Node:
  def  __init__(self,value):
      self.value = value
      self.right = None
      self.left = None

class BST:
  def __init__(self):
      self.root = None

  def insert(self,value):
      new_node = Node(value)
      if self.root is None:
          self.root =  new_node
          return True
      temp =self.root
      while(True):
        if new_node.value == temp.value:
             return False
        if new_node.value < temp.value:
            if temp.left is None:
                temp.left = new_node
                return True
            temp = temp.left
        else:
            if temp.right is None:
                temp.right = new_node
                return True
            temp = temp.right
  def search(self, value):
      temp = self.root
      while (temp is not None):
        if value < temp.value:
              temp = temp.left
        elif value > temp.value:
              temp = temp.right
        else:
            return True
      return False

  def minimum(self, curr_node):
      while(curr_node.left is not None):
          curr_node= curr_node.left
      return curr_node.value



t = BST()
t.insert(2)
t.insert(1)
t.insert(3)
#print(t.root.value)
#print(t.root.left.value)
#print(t.root.right.value)
print(t.search(1))
#print(t.search(5))
#print(t.minimum(t.root))







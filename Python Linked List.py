# Node class
class Node():
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node

# .get_value() and .get_next_node() methods which return the corresponding values from self.
  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

# allows you to update the link to the next node.
  def set_next_node(self, next_node):
    self.next_node = next_node

"""
#instance of Node
my_node = Node(44)
#value of my_node using .get_value
print(my_node.get_value())
"""

class LinkedList:
  def __init__(self, value = None):
    self.head_node = Node(value)
#peek at the first node in the list.
  def get_head_node(self):
    return self.head_node

import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value >= self.value:
      if self.right:
        self.right.insert(value)
      else: self.right = BinarySearchTree(value)
    elif value < self.value:
      if self.left:
        self.left.insert(value)
      else: self.left = BinarySearchTree(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False
    if target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        return False

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

# DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print(self, node):
      if self.left:
        self.left.in_order_print(self.left)

      print(self.value)

      if self.right:
        self.right.in_order_print(self.right)
      

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
      storage = Queue()
      current = self

      while current:
        print(current.value)
        if current.left:
          storage.enqueue(current.left)
        if current.right:
          storage.enqueue(current.right)
        current = storage.dequeue()
      

      


  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
      storage = Stack()
      current = node

      while current:
        print(current.value)
        if current.right:
          storage.push(current.right)
        if current.left:
          storage.push(current.left)
        current = storage.pop()

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
    print(self.value)
    if self.left:
      self.left.in_order_print(self.left)
    if self.right:
      self.right.in_order_print(self.right)

  # Print Post-order recursive DFT
  def post_order_dft(self, node):

    if self.left:
      self.left.post_order_dft(self.left)
    if self.right:
      self.right.post_order_dft(self.right)
    print(self.value)

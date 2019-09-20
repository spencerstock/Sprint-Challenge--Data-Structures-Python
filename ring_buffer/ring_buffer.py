class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = [None]*capacity
    self.oldest = 0

  def append(self, item):
    self.storage[self.oldest] = item
    if (self.oldest < self.capacity-1):
      self.oldest += 1
    else:
      self.oldest = 0

  def get(self):
    result = []
    for i in self.storage:
      if i:
        result.append(i)
    return result

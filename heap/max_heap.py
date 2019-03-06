class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # set value to the end of the array
    self.storage.append(value)
    # execute bubble-up to correctly place element
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    # store element to be deleted to index 0
    removed_item = self.storage[0]
    # use 'del' operator to delete the item stored to index 0
    del self.storage[0]
    # execute sift down to rearrange max heap
    self._sift_down(0)
    # return deleted item
    return removed_item

  def get_max(self):
    # first value should be the biggest of the heap
    return self.storage[0]

  def get_size(self):
    # returns the length of the heap
    return len(self.storage)


  # called as a helper function in insert
  # "bubble up" the newly inserted element to a valid spot in the heap 
  def _bubble_up(self, index):
    # we'll use the child-to-parent formula here
    # loop until parent index == 0
    while (index - 1) // 2 >= 0:
      # child has access to parent at this point
      # compare the child's value against its parent's value
      #  if child's value > parents value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # swap these two elements via their indices
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      # repeat this process until the child no longer needs to be swapped with it's parent
      # update index to be the parent's index
      index = (index -1) // 2


  # called as a helper function in delete
  # "sifts down" the element at the top of the heap
  def _sift_down(self, index):
    # while child index is less than last index
    while index * 2 + 1 <= len(self.storage) - 1:
      # if second child is less than the last index
      if index * 2 + 2 > len(self.storage) - 1:
        # make the first child the max
        maxValue = index * 2 + 1
        # if the second child is greater than the first child
      elif self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
        # make the second child the max
        maxValue = index * 2 + 1 
      else: 
        maxValue = index * 2 + 2

      if self.storage[maxValue] > self.storage[index]:
        self.storage[maxValue], self.storage[index] = self.storage[index], self.storage[maxValue]
      index = maxValue

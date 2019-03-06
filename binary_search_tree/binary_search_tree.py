class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # prevent duplicate
    if self.value == value:
      return False
    # if value thats being inserted is less than current value
    elif value < self.value:
    # check down the left branch
      if self.left:
        # Recursively run insert again to check if there is a another node to compare
        return self.left.insert(value)
      else: 
        # Insert value if there no more nodes to compare
        self.left = BinarySearchTree(value)
        return True
    # if the value is greater than the current node:
    else:
      # check right branch
      if self.right:
        # Recursivley run insert again to check if there is another node to compare
        return self.right.insert(value)
      else:
        # Insert the value if there is no more nodes to compare
        self.right = BinarySearchTree(value)
        return True

  def contains(self, value):
    # Check current node to see if the value matches
    if value == self.value:
      return True
    elif value < self.value:
      # If the value is less than the current node, check down the left branch
      if self.left:
        # If left branch exists, recursively run contains() to check the next node down in the left branch
        return self.left.contains(value)
        # Return false if value is not found
      else:
        return False

    else: 
      # If right branch exists, recursively run contains() to check the next node down in the right branch
      if self.right:
        return self.right.contains(value)
      # return false if value is not found
      else:
        return False


  def get_max(self):
    curr_max = self
    # set max to 0
    max_ = 0
    # while looking at current max ; curr_max
    while curr_max:
      # compare current max to maximum value found
      if curr_max.value > max_:
        #if current max is bigger than max, set current max value to the maximum value
        max_ = curr_max.value
        # set current max to next node to the right
        curr_max = curr_max.right
    # return maximum value
    return max_

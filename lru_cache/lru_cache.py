import collections

class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.cache = collections.OrderedDict()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # try to get the key-value pair from cache
    try:
      value = self.cache.get(key)
      # move key-value pair to front of cache(?)
      self.cache.move_to_end(key, last = True)
      return value
    except KeyError:
      return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    # check and see if key is already in cache
    if not self.cache.get(key):
      # check if the cache is at maximum
      if len(self.cache) >= self.limit:
        # remove the latter accessed key
        self.cache.popitem(last = False)
    # add key-value pair tp cache
    self.cache[key] = value
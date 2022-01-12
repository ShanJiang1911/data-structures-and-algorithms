class hashtable:

    def __init__(self, size=1024):
        self.buckets = [None] * size

    def add(self, key, value):
        index = self.hash(key)
        if self.buckets[index]:
          for i in self.buckets[index]:
            if i[0] == key:
              i[1] = value
              break
          else:
            self.buckets[index].append([key, value])
        else:
          self.buckets[index] = []
          self.buckets[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
          raise KeyError()
        else:
          for i in self.buckets[index]:
            if i[0] == key:
              return i[1]
          raise KeyError()

    def contains(self, key):
        index = self.hash(key)
        if index in self.buckets[index]:
          return True
        else:
          return False

    def hash(key, size=1024):
        #sum the ascii values of characters in key
        # multiply by 599 (or) another prime number
        # index = modulus by len of array
        ascii_values = []
        for char in key:
          ascii_values.append(ord(char))
        index = sum(ascii_values) % size
        return index

    print(hash("Hello World"))

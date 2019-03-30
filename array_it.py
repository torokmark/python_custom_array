class ArrayIt:
  def __init__(self, values = []):
    self.array = values
    self.current = 0

  def __getitem__(self, key):
    return self.array[key]

  def __iter__(self):
    return self

  def __next__(self):
    try:
      self.current += 1
      return self.array[self.current - 1]
    except IndexError:
      self.current = 0
      raise StopIteration

it = ArrayIt([1, 2, 3, 4, 5, 6, 7])
print(it[2]) # => 3
for i in it:
  if i == 5:
    break
  print(i) # => 1, 2, 3, 4

for i in it:
  print(i) # => 6, 7

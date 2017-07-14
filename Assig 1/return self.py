class Foo:

  def __init__(self):
    x = 5

  def bar(self):
    self.y = x
    return self

a = Foo()

print(a.bar())


# 闭包
def test():
  a = 20
  def fnc():
    print(a + 10)
  return fnc

go = test()

go()


# global
s = 10

def test1():
  global s
  s = s + 10
  print(s)

test1()
# 装饰器

import time

def log(func):
  def wrapper(*args, **kw):
      print('call %s():' % func.__name__)
      return func(*args, **kw)
  return wrapper

@log # 装饰器
def f1():
  print(time.time())
  print('this is a function')

f1()
# 函数返回多个值
def my_print(a,b,c):
  return a,b,c

res = my_print('haha','bbb','qqqqq')

print(res) # ('haha', 'bbb', 'qqqqq') 元组

# 返回对象
def return_obj(name,age,sex):
  return {'name':name,'age':age,'sex':sex}

FinGet = return_obj('FinGet',23,'男')

print(FinGet)
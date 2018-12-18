# 面向对象 封装、继承、多态

class Student():
  # 属性 类变量 实例共有
  mouse = '嘴巴'
  hand = '手'

  # 构造函数 实例化时 就会自动调用
  def __init__(self, name, age):  
    # 实例变量
    self.name = name
    self.age = age
    print(name)

    # 访问类变量
    print(Student.mouse)
    print(self.__class__.hand)
    return
  
  # 行为方法
  def get_name(self):
    print(self.name)

# 实例化
student = Student('finget', 23)

print(student.get_name())
print(student.mouse)
print(student.__dict__) # 打印实例变量

""" 
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方 
"""
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
    return
  
  # 实例方法
  def mark(self, score):
    # 私有变量
    self.__score = score
    print(self.name)

# 实例化
student = Student('finget', 23)
student.mark(60)
print(student.__dict__)
# 间接读取私有变量
print(student._Student__score)
# {'name': 'finget', 'age': 23, '_Student__score': 60}

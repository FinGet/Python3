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
    # print(name)

    # 访问类变量
    # print(Student.mouse)
    # print(self.__class__.hand)
    return
  
  # 类方法
  @classmethod
  def class_fnc(cls):
    print(cls.hand)

  # 静态方法
  @staticmethod
  def static_fnc():
    print('这是静态方法')

  # 实例方法
  def get_name(self):
    print(self.name)

# 实例化
student = Student('finget', 23)
# print(student.get_name())
Student.class_fnc()
student.static_fnc()

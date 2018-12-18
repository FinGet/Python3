# 继承 python 允许多继承

class People():
  handle = '双手'
  mouse = '嘴巴'

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def go(self):
    print('走路')
  
  def eat(self, food):
    print('吃'+ food)

# 继承People
class Student(People):
  
  def __init__(self, name, age):
    super(Student,self).__init__(name,age)

  def do_work(self, category):
    print('做'+category+'作业')
  
  # 重写
  def eat(self, food):
    print('吃很多'+ food)
  

student = Student('FinGet', 23)
print(student.name)
print(Student.handle)
student.go()
student.eat('肉嘎嘎')# 子类调用重写方法  
super(Student,student).eat('肉嘎嘎') #用子类对象调用父类已被覆盖的方法
student.do_work('语文')
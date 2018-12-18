# 参数

# 必需参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

# str必需传入
def printme( str ):
   '''打印任何传入的字符串'''
   print (str)
   return
 
#调用printme函数
printme('hahaha') 

# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=23, name="FinGet" )


# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。
def printinfo1( name, age = 23 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo1( age=24, name="FinGet" )
print ("------------------------")
printinfo1( name="FinGet" )

# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数

""" def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression] """
  
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

def printinfo2( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo2( 70, 60, 50 )

# 还有一种就是参数带两个星号 **基本语法如下：
""" def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression] """

# 加了两个星号 ** 的参数会以字典的形式导入

def printinfo3( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo3(1, a=2,b=3)


# 声明函数时，参数中星号 * 可以单独出现，例如:

def f(a,b,*,c):
    return a+b+c

# 如果单独出现星号 * 后的参数必须用关键字传入。

""" def f(a,b,*,c):
    return a+b+c

f(1,2,3)   # 报错

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given

f(1,2,c=3) # 正常
6
"""
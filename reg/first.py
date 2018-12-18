""" 
re.match(pattern, string, flags=0)
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	  标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
"""

import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# <re.Match object; span=(0, 3), match='www'>
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

""" 
(0, 3)
None
"""

# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

""" 
re.search方法 re.search 扫描整个字符串并返回第一个成功的匹配。
re.search(pattern, string, flags=0)
"""
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配



"""  
正则表达式修饰符 - 可选标志
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""

line = "Cats are smarter than dogs";
 
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
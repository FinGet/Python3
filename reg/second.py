"""  
compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
"""
import re

pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)

s = 'abc, acc, adc, aec, afc, agc'
r = re.findall('a[cf]c',s)
print(r)

# 取反
sr = re.findall('a[^cf]c',s)
print(sr)

"""  
检索和替换
re.sub(pattern, repl, string, count=0)

pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
"""
phone = "2004-959-559 # 这是一个电话号码"
 
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)
 
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)


"""  
re.finditer
re.finditer(pattern, string, flags=0)
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
"""
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() )

"""  
re.split
split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
re.split(pattern, string[, maxsplit=0, flags=0])
分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
"""

print(re.split('\W+', 'runoob, 123, runoob .'))
print(re.split('\W+', 'runoob, 123, runoob .',1))
print(re.split('a*', 'hello world'))
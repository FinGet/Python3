# 循环

num = int(input('输入数字：'))

while num>5:
    print('num='+ str(num))

arr_list = [1,2,3,4,5,6]

for item in arr_list:
    print(item)
else:
    print('已经遍历完了')

for x in range(0,10):
    print(x, end='')

for x in range(0,10,2):
    print(x, end = '|')

for x in range(10,0,-2):
    print(x, end = '|')


a = [1,2,3,4,5,6,7,8,9]

for i in range(0,len(a),2):
    print(a[i]) 

b = a[0:len(a):2]
print(b)
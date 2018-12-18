# 函数
a = 1.12386
print(round(a,2))
# 函数没有return 就会返回一个 None
def add(a, b):
  return a + b

res = add(1,2)

print(res)

# sys.setrecursionlimit(10000) 设置递归次数
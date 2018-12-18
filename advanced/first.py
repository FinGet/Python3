from enum import Enum
# 枚举
class VIP(Enum):
  # 标签不能重复
  YELLOW = '1'
  GREEN = '2'
  BLACK = '3'
  RED = '4'
  YELLOW_ALIAS = '1'
print(VIP.YELLOW)
print(VIP.YELLOW_ALIAS)
print(VIP.YELLOW.value)

# VIP.YELLOW = 5 # 报错

for v in VIP:
  print(v)

for v in VIP.__members__.items():
  print(v)
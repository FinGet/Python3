from enum import IntEnum
# 枚举
class VIP(IntEnum):
  # 标签不能重复
  YELLOW = '1'
  # GREEN = 'str' 不能是字符串
  BLACK = '3'
  RED = '4'
  YELLOW_ALIAS = '1'

print(VIP.YELLOW)
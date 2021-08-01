"""
要求输出由小写字母v组成的大V。
输出描述：
v   v

 v v

  v
"""
# _*_ coding:utf-8 _*_
def output_v():
  a = 'v   v'
  b = 'v v'
  c = 'v'
  d = a.center(5) + '\n' + b.center(5) + '\n' + c.center(5)  # str.center(n, '')默认参数为空格补齐，可以不写
  print(d)
output_v()

#导入模块的一些语法
from random import randint # from 模块名 import 函数名，导入模块里的一个方法或变量
from math import * # from 模块名 import * ,导入模块里的'所有'(并不是所有的都能导进来)方法和变量
import datetime as dt #导入一个模块并给她起一个别名
from copy import deepcopy as dc #导入模块里的一个方法或变量，并给她一个别名

'''
1 os模块
os 全称 operation System操作系统
os 模块提供的方法就是用来调用操作系统里的方法
'''
# 这些是我的文件，你们可以换成自己有的文件或文件夹名
# 都是需要打印才能看到的，后面的我就没有使用print去输出了
print(os.path.abspath('01.高阶函数.py'))# 获取绝对路径
print(os.path.dirname(os.path.abspath(__file__)))# 获取该文件的父节点
print(os.path.isdir('01.高阶函数.py'))# False,判断是否是文件夹
print(os.path.isfile('01.高阶函数.py'))# True 判断是否是文件
print(os.path.exists('01.高阶函数.py'))# True 判断是否存在
# os.getcwd() # 获取当前的工作目录,即当前python脚本工作的目录
# os.chdir('test') # 改变当前脚本工作目录，相当于shell下的cd命分
# os.rename('毕业论文.txt','毕业论文-最终版.txt') #文件重命名
# os.remove('毕业论文.txt') # 删除文件
# os.rmdir('demo') # 删除空文件夹
# os.removedirs('demo') #删除空文件夹
# os.mkdir('demo') # 创建一个文件夹
# os.listdir('C:\\')#列出指定目录里的所有文件和文件夹
# os.name # nt- >widonws posix- >L inux/Unix或者MacOS
# os.environ #获取到环境配置

'''
2 math模块
数学相关计算的模块
'''
import math

print(math.pi) # 3.141592653589793
print(math.factorial(5))  # 120 求阶乘
print(math.pow(2, 10))  # 1024.0 幂运算
print(math.floor(15.999))  # 15 向下取整
print(math.ceil(14.001))  # 15 向上取整
print(math.sin(math.pi / 6))# 1024.0
print(math.cos(math.pi / 3))# 0.5000000000000001
print(math.tan(math.pi / 4))# 0.9999999999999999

'''
3 random模块
和随机数相关的模块
'''
import random
# 注意开闭区间
print(random.randint(2, 9))#randint(a,b)用来生成[a,b]的随机整数
print(random.randrange(2, 9))#randrange(2,9)用来生成[a,b)的随机整数
print(random.random())# 用来生成[0,1)的随机浮点数
print(random.choice(range(2, 9)))# 用来在可迭代对象里随机抽取一个数据
# 用来在可迭代对象里随机抽取n个数据
print(random.sample(range(10), 2))

'''
4 datetime模块
'''
import datetime as dt

print(dt.datetime.now())# 获取当前日期时间
print(dt.date(2010, 12, 21))# 2010-12-21 创建一个日期
print(dt.time(12, 12, 12))# 12:12:12 创建一个时间
print(dt.datetime.now() + dt.timedelta(3))# 计算三天后的时间

'''
5 time模块
'''
import  time
print(time.time())# 获取从1970-01-01 00:00:00 UTC 到现在时间的秒数
print(time.strftime('%Y-%m-%d %H:%M:%S'))# 按照格式打印时间
print(time.ctime())# ctime()要的是一个时间戳
print('hello')
time.sleep(10)# 睡眠10秒
print('world')

'''
6 hashlib和hmac模块
'''
import  hashlib
import hmac
# 这两个模块是用来进行数据加密的
# hashlib模块里主要支持两个算法 md5 和 sha 加密
# 加密方式：单向加密，只能加密，不能解密md5和sha

# 需要将要加密的内容转换为二进制
x = hashlib.md5()
x.update('abc'.encode('utf8'))
print(x.hexdigest())# 900150983cd24fb0d6963f7d28e17f72

h1 = hashlib.sha1('123456'.encode())
print(h1. hexdigest())# 7c4a8d09ca3762af61e59520943dc26494f8941b
h2 = hashlib.sha224( '123456'.encode())# 224位，一个十六进制占4位
print(h2. hexdigest())# f8cdb04495ded47615258f9dc6a3f4707fd2405434fefc3cbf4ef4e6
h3 = hashlib.sha256('123456'.encode())
print(h3. hexdigest())# 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
h4 = hashlib.sha384('123456'.encode())
print(h4. hexdigest())# 0a989ebc4a77b56a6e2bb7b19d995d185ce44090c13e2984b7ecc6d446d4b61ea9991b76a4c2f04b1b4d244841449454

# hmac加密可以指定秘钥
h = hmac.new('h'.encode(),'你好'.encode())# 使用'h'对'你好'进行加密
print(h.hexdigest())
'''
7 calendar模块
日历模块
'''
import  calendar
# 可以点进帮助文档看看，还有很多有关日历的方法
print(calendar.calendar(2021))# 打印日历
print(calendar.isleap(2020))# True 判断是否闰年

'''
使用第三方模块
'''
# 注意这是在Terminal终端输入的，当然也可以使用cmd
# pip install <package_name> 用来下载一个第三方模块
# pip uninstall <package_name> 用来删除一个第三方模块
# pip list 用来列出当前模块安装了哪些模块
# pip freeze 用来列出当前环境安装的模块名和版本号
# pip install <package_name> -i <url>路径 从指定的地址下载包（临时改的）
# pip freeze > file_name 将安装的模块名和版本号重定向输出到指定的文件
# pip install -r flie_name 读取文件里的模块名和版本号并安装
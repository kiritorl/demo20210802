class Person(object):
    def __init__(self):
        self.__name = None   # NULL
        pass

    pass

name = 'zhang'
name1 = "zhang1"
name2 = '''zhang nb nnn !
sdffad!'''
'''
三个单引号或三个双引号
多行注释
或者多行字符串定义
'''
print('1234', '12', '234', sep="-", end="***")
print('1234', '12', '234', sep="-", end="\n")  # sep分隔符end结束符默认换行

# 字符串类型
str1 = "zhang age is %d %s %.2f" % (18, 'account', 2.145432)
print(str1)

str2 = "zhang age is {0} {1} {2}".format(18, 'account', 2.145432)
print(str2)

import sys

print(sys.argv)

result = int(sys.argv[1]) + int(sys.argv[2])

print(result)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：basic.py

# if you want to print chinese,mast set coding （before 3.x）
# print("中文")



# Python 标识符
# 在 Python 里，标识符由字母、数字、下划线组成。
# 在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
# Python 中的标识符是区分大小写的。
# 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
# 以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
# Python 可以同一行显示多条语句，方法是用分号 ; 分开，如：

# print 'hello';print 'again'



# 多行语句
# Python语句中一般以新行作为语句的结束符。
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：

# total = 1 + \
#         2 + \
#         3
# print(total)



# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：

# days = ['Monday', 'Tuesday', 'Wednesday',
#         'Thursday', 'Friday']
# print days




# Python 引号
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

# word = 'word'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落。
# 包含了多个语句"""




# Python空行
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分。



# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

# #import sys; x = 'runoob'; sys.stdout.write(x + '\n')



# Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
# print('a'); print('b')
# print('c'),
# print('d'),
# print 'e','f'




# 变量赋值
# Python 中的变量赋值不需要类型声明。
#
# 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
#
# 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#
# 等号（=）用来给变量赋值。
#
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
# counter = 100 # 赋值整型变量
# miles = 1000.0 # 浮点型
# name = "John" # 字符串
# print counter
# print miles
# print name



# 多个变量赋值
# Python允许你同时为多个变量赋值。例如：

a = b = c = 1
# 以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。

# 您也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "john"
# 以上实例，两个整型对象 1 和 2 分别分配给变量 a 和 b，字符串对象 "john" 分配给变量 c。



# 标准数据类型
# 在内存中存储的数据可以有多种类型。
# 例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。
# Python 定义了一些标准类型，用于存储各种类型的数据。
# Python有五个标准的数据类型：
#
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）



# Python支持四种不同的数字类型：
#
# int（有符号整型）
# long（长整型[也可以代表八进制和十六进制]）
# float（浮点型）
# complex（复数）



# str = 'Hello World!'
#
# print str           # 输出完整字符串
# print str[0]        # 输出字符串中的第一个字符
# print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
# print str[2:]       # 输出从第三个字符开始的字符串
# print str * 2       # 输出字符串两次
# print str + "TEST"  # 输出连接的字符串



# Python列表
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
# 列表用 [ ] 标识，是 python 最通用的复合数据类型。
# 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
# print list               # 输出完整列表
# print list[0]            # 输出列表的第一个元素
# print list[1:3]          # 输出第二个至第三个元素
# print list[2:]           # 输出从第三个开始至列表末尾的所有元素
# print tinylist * 2       # 输出列表两次
# print list + tinylist    # 打印组合的列表




# Python元组
# 元组是另一个数据类型，类似于List（列表）。
# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
# tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
# tinytuple = (123, 'john')
# print tuple               # 输出完整元组
# print tuple[0]            # 输出元组的第一个元素
# print tuple[1:3]          # 输出第二个至第三个的元素
# print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
# print tinytuple * 2       # 输出元组两次
# print tuple + tinytuple   # 打印组合的元组


# 以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：
# tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tuple[2] = 1000    # 元组中是非法应用
# list[2] = 1000     # 列表中是合法应用


# Python 字典（JAVA Map）
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
# print dict['one']          # 输出键为'one' 的值
# print dict[2]              # 输出键为 2 的值
# print tinydict             # 输出完整的字典
# print tinydict.keys()      # 输出所有键
# print tinydict.values()    # 输出所有值
























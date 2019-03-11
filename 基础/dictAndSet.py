print('Python之什么是dict')
'''
类似java中的map集合

花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。
'''
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul':75
}
print(d)
print('Python之访问dict')
'''
 d[key] 的形式来查找对应的 value，这和 list 很像，
 不同之处是，list 必须使用索引返回对应的元素，而dict使用key：
 
 注意: 通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError。
'''
print d['Bart']

'''
要避免 KeyError 发生，有两个办法：

一是先判断一下 key 是否存在，用 in 操作符：
if 'Paul' in d:
    print d['Paul']
	
如果 'Paul' 不存在，if语句判断为False，自然不会执行 print d['Paul'] ，从而避免了错误。

二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：

>>> print d.get('Bart')
59
>>> print d.get('Paul')
None
'''
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print 'Adam:',d['Adam']
print 'Lisa:',d['Lisa']
print 'Bart:',d['Bart']

print('Python中dict的特点')
'''
dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。
而list的查找速度随着元素增加而逐渐下降。

不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，
list正好相反，占用内存小，但是查找速度慢。

由于dict是按 key 查找，所以，在一个dict中，key不能重复。

dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样：

dict的第三个特点是作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，
都可以作为 key。但是list是可变的，就不能作为 key。
'''
d = {
    95: 'Adam',
    85:'Lisa',
    59: 'Bart'
}
print(d[95])

print('Python更新dict')

'''
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
d[72] = 'Paul'
print(d)
'''
print('Python之 遍历dict')
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for a in d:
    print a+":",d[a],

print('Python中什么是set')
'''
set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：

>>> s = set(['A', 'B', 'C'])
可以查看 set 的内容：

>>> print s
set(['A', 'C', 'B'])

set会自动去掉重复的元素
'''
s = set(['Adam', 'Lisa','Bart', 'Paul'])
print(s)

print('Python之 访问set')
'''
由于set存储的是无序集合，所以我们没法通过索引来访问。

访问 set中的某个元素实际上就是判断一个元素是否在set中。
'''
s = set(['adam','bart'])
print 'adam' in s
print 'bart' in s

print('Python之 set的特点')
'''
set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。

set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。

最后，set存储的元素也是没有顺序的。
'''
print('Python之 遍历set')
'''
注意: 观察 for 循环在遍历set时，元素的顺序和list的顺序很可能是不同的，而且不同的机器上运行的结果也可能不同。
'''
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
#    print x
#    print x[0]
#    print x[1]
    print x[0]+':'+str(x[1])

print('Python之 更新set')
'''
由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：

一是把新的元素添加到set中，二是把已有元素从set中删除。

添加元素时，用set的add()方法：
如果添加的元素已经存在于set中，add()不会报错，但是不会加进去了：
删除set中的元素时，用set的remove()方法：
如果删除的元素不存在set中，remove()会报错：
所以用add()可以直接添加，而remove()前需要判断。
'''
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
     if name in s:
          s.remove(name)
     else:
          s.add(name)
print s
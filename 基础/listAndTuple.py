print('Python创建list')
'''
list是一种有序的集合，可以随时添加和删除其中的元素。
直接用 [ ] 把list的所有元素都括起来，就是一个list对象。
通常，我们会把list赋值给一个变量，这样，就可以通过变量来引用list
'''
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

'''
list中包含的元素并不要求都必须是同一种数据类型，我们完全可以在list中包含各种数据
'''
L = ['Michael', 100, True]
print(L)
print([])

print('Python按照索引访问list')
'''
报错了！IndexError意思就是索引超出了范围
使用索引时，千万注意不要越界。
'''
M['A','B','C']
print(M[0])
print(M[1])
print(M[2])

print('Python之倒序访问list')
print(M[-1])

print('Python之添加新元素')
'''
list 的 append() 方法，把新同学追加到 list 的末尾
list的 insert()方法，它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素
'''
L.insert(2,'Paul')
print (L)

print('Python从list删除元素')
'''
list的pop()方法删除 pop()方法总是删掉list的最后一个元素，并且它还返回这个元素
先定位删除数据的位置。由于数据位置的索引是2，因此，用 pop(2)把数据删掉
'''
L.pop(2)
print (L)

print('Python中替换元素')
'''
对list中的某一个索引赋值，就可以直接用新的元素替换掉原来的元素，list包含的元素个数保持不变。
'''
L[2] = 'Paul'
L[-1]='A'
print (L)
print('Python之创建tuple')
'''
tuple是另一种有序的列表，中文翻译为“ 元组 ”。
tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。
创建tuple和创建list唯一不同之处是用( )替代了[ ]
这个 t 就不能改变了，tuple没有 append()方法，也没有insert()和pop()方法
获取 tuple 元素的方式和 list 是一模一样的，我们可以正常使用 t[0]，t[-1]等索引方式访问元素，但是不能赋值成别的元素
'''
t = ('Adam', 'Lisa', 'Bart')
print(t)

print('Python之创建单元素tuple')
'''
包含 0 个元素的 tuple，也就是空tuple，直接用 ()表示
()既可以表示tuple，又可以作为括号表示运算时的优先级，结果 (1) 被Python解释器计算出结果 1，
导致我们得到的不是tuple，而是整数 1
Python 规定，单元素 tuple 要多加一个逗号“,”，这样就避免了歧义
'''
print(())
print((1,))

print('Python之“可变”的tuple')
'''
“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，
但指向的这个list本身是可变的！
'''

#条件判断和循环
print('Python之if语句')
'''
注意: Python代码的缩进规则。具有相同缩进的代码被视为代码块，
上面的3，4行 print 语句就构成一个代码块（但不包括第5行的print）。
如果 if 语句判断为 True，就会执行这个代码块。

缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，
否则很容易造成因为缩进引起的语法错误。

注意: if 语句后接表达式，然后用:表示代码块开始。

如果你在Python交互环境下敲代码，还要特别留意缩进，并且退出缩进需要多敲一行回车
'''
age = 20
if age >= 18:
    print ('your age is', age)
    print ('adult')
print ('END')

print('Python之 if-else')
'''
利用 if ... else ... 语句，我们可以根据条件表达式的值为 True 或者 False ，
分别执行 if 代码块或者 else 代码块。
注意: else 后面有个“:”。
'''
score = 55
if score>=60:
    print ('passed')
else:
    print ('failed')
	
	
print('Python之 if-elif-else')
'''
elif 意思就是 else if。这样一来，我们就写出了结构非常清晰的一系列条件判断。

特别注意: 这一系列条件判断会从上到下依次判断，如果某个判断为 True，
执行完对应的代码块，后面的条件判断就直接忽略，不再执行了。
'''
score = 85

if score>=90:
    print 'excellent'
elif score>=80:
    print 'good'
elif score>=60:
    print 'passed'
else:
    print 'failed'
	
print('Python之 for循环')
'''
Python的 for 循环就可以依次把list或tuple的每个元素迭代出来
'''
L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print (name)
'''
注意:  name 这个变量是在 for 循环中定义的，意思是，
依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体（就是缩进的代码块）。
'''
L = [75, 92, 59, 68]
sum = 0.0
for a in L:
    print(a)
    sum+=a
print (sum)
print (sum / 4)

print('Python之 while循环')
'''
N = 10
x = 0
while x < N:
    print x
    x = x + 1

while循环每次先判断 x < N，如果为True，则执行循环体的代码块，否则，退出循环。

在循环体内，x = x + 1 会让 x 不断增加，最终因为 x < N 不成立而退出循环。
'''
sum = 0
x = 1
while x<=100:
    sum+=x;
    x+=1;
print (sum)

print('Python之 break退出循环')
'''
在循环体内直接退出循环，可以使用 break 语句
'''
sum = 0
x = 1
n = 1
while True:
    sum=sum+x
    x=x*2
    n=n+1
    if n > 20:
      break
print sum

print('Python之 continue继续循环')
'''
还可以用continue跳过后续循环代码，继续下一次循环
'''

print('Python之 多重循环')
'''
for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y
x 每循环一次，y 就会循环 3 次，这样，我们可以打印出一个全排列
'''
for x in [1,2,3,4,5,6,7,8,9]:
    for y in [1,2,3,4,5,6,7,8,9]:
        if x<y:
           print(x*10+y) 
		   

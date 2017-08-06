## 装饰器

### 什么是装饰器

> http://egon09.blog.51cto.com/9161406/1836763
> http://www.cnblogs.com/alex3714/articles/5765046.html

装饰器本质上说一个函数。用于装饰器他函数，简单的说就是给其他函数添加新的附加功能。

应用原则：
装饰器对被装饰函数完全透明，即：
1. 不能修改被装饰函数的源代码
2. 不能修改被装饰函数的调用方式


实现装饰器的知识存储：
1. 函数即 "变量"
2. 高阶函数
  + 把函数名作为实参传入另外一个函数
  + 返回值中包含函数名
3. 嵌套函数

高阶函数 + 嵌套函数 == 实现 ==> 装饰器



#### 函数即 "变量"

没有函数名的函数
lambda x:x*3


### 迭代器和生成器

#### 列表生成器

生成器： generator

使代码更简洁
受内存限制，所创建列表容量有限。
使用生成器，不必预创建完整列表，当调用的时候才会生成数据，从而节约内存空间。也因为此，生成器不支持切片或使用 `a[2]` 之类的列表操作。
生成器不保存之前生成过的数据，也不会预先生成之后的数据，只保留当前位置数据。


生成列表
```python
>>> [ i*2 for i in range(10) ]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

a=[]
for i in range(10)
    a.append(i*2)

>>> [ i*2 for i in range(10) if i %2==0 ]
[0, 4, 8, 12, 16]

>>> [ abs(i) for i in range(10) if i %2==0 ]
[0, 2, 4, 6, 8]


```

生成器
```python
>>> ( i for i in range(10) if i %2==0 )
<generator object <genexpr> at 0x02DFA620>
>>> print ( i for i in range(10) if i %2==0 )
<generator object <genexpr> at 0x02CE63A0>

>>> gen=( i for i in range(10) if i %2==0 )
>>> for b in gen:
	print b
0
2
4
6
8

# 生成器也不是可以准备任意多的 item
>>> gen=( i for i in range(100000000000))

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    gen=( i for i in range(100000000000))
OverflowError: range() result has too many items


```

##### 生成器方法

# python 3.x
gen.__next__()
# python 2.7
gen.next()


##### 通过 yield 创建生成器

在构造函数的时候，在函数内使用 `yield` 返回结果，可以构造一个生成器

赋值语句：
a,b=b,a_b

相当于：
 t=(b,a+b)
 a=t[0]
 b=t[1]


### 迭代器

可以直接 for 循环的数据类型和结构包括：
+ ...


可以直接作用于 for 循环的对象统称为 可迭代对象( Iterable )
可以使用 `isinstance()` 判断一个对象是否为可迭代对象。

```python

from collections import Iterable

isinstance([],Iterable)

# 举例
+ ...
```

> 可以被 next() 函数调用并返回下一个值的对象，统称为迭代器(Iterator)。

可以使用 `isinstance()` 判断一个对象是否为迭代器对象。

```python

>>> from collections import Iterator
>>>
>>> isinstance(( i for i in xrange(10)),Iterator)
True

```

使用 `iter()` 函数，可以将可迭代对象转换为迭代器，表示一个惰性计算序列。

```python
>>> a=[1,2,3,4]
>>>
>>> isinstance(a,Iterator)
False
>>> iter_a=iter(a)
>>>
>>> isinstance(iter_a,Iterator)
True
>>> iter_a.next()
1
>>> next(iter_a)
2
```

在 python 中， Iterator 对象表示一个数据流， Iterator 对象可以被 `next()` 函数调用并不断返回下一个数据，知道没有数据时抛出 `StopIteration` 错误。可以把这个数据流看作一个有序序列，但不能确切知道序列长度，只能不断通过 `next()` 函数实现按需计算下一个数据，所以 Iterator 的计算是惰性的，只有在需要返回下一个数据时他才会计算。

Iterator 甚至可以表示一个无限大的数据流，而 `列表` 由于内存原因，无法办到。


#### 小结

凡是可作用于 `for` 循环的对象都是『可迭代对象 Iterable 』
凡是可作用于 `next()` 函数的对象都是『迭代器对象 Iterator 』，他们表示一个惰性计算序列。
集合数据类型(ex. list,dict,str,set)等是可迭代对象，但不是迭代器对象；但可以通过 `iter()` 方法转换为迭代器对象。
python 的 `for` 循环本质上就是通过不断的调用 `next()` 方法实现的。


### 内置方法


### 装饰器
http://www.cnblogs.com/wupeiqi/articles/4980620.html



### Json & pickle 数据序列化

参考 http://www.cnblogs.com/alex3714/articles/5161349.html

#### Json 序列化

import json
序列化
str=json.dumps(data)
反序列化
data=json.loads(str)

#### pickle 序列化

import pickle
序列化
bin_str=pickle.dumps(data)
bin_str=pickle.dump(data,f_obj)

反序列化
data=pickle.loads(bin_str)
f_obj=open(file.'rb')
data=pickle.load(bin_str,f_obj)

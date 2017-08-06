# 常用模块学习

> www.cnblogs.com/alex3714/articles/5161349html

## import 的方法

import module
import module1,module2
from module import func_or_var
from module import func1,func2,var1,var2
from module import func_or_var as alias_name
from package import module
from path.package import module


## import 搜索路径

import 的本质就是将导入的代码解释一次，放入本地内存空间
from import 相当于在本地文件写一次所导入的内容
导入包的本质就是解释了一次包目录下的 `__init__.py`

import 的时候，python 会优先使用当前目录下的模块。
当前目录下没有该模块的时候，会在 sys.path 列表中的路径从左到右搜索。
遵循先找到先使用的方法。

因此，在需要引用本地工程目录中的模块时，可以将本地路径添加到 sys.path 中，可以使用

+ 追加： sys.path.append(path)
+ 插入： sys.path.insert(path)



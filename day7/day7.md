# 静态方法
  @staticmethod
  静态方法实际上是取消 类方法与类的关联。将类方法变成一个单纯的函数。
  类中的函数只是名义上属于类，但是不能访问内中的任何东西。


# 类方法
  @classmethod
  只能访问类变量，不能访问实例变量


# 属性方法
  @property
  把一个方法变成一个静态属性


# 反射
  通过字符串映射或修改程序运行时的状态、属性、方法，也偶一下4个方法
  + hasattr(object, name_string): 判断 object 对象中， 是否还有 name_string 对应的方法或属性。如果有则返回 True，反之 返回 False。
  + getattr(object, name_string): 获取 object 对象中 ，name_string 对应方法的内存地址或属性的值
  + setattr(object, key , value): 为 object 新建一个方法或属性，或修改一个已存在的方法或属性的值。 相当于 object.key = value。
  + delattr(object ,name_string): 删除 object 中的一个方法或属性。


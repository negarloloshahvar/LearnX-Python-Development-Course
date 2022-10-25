class MyClass:
    a = 1
    b = 2

instance = MyClass()
print(repr(instance))
print(instance.__dir__())
print(type(instance).__dict__)

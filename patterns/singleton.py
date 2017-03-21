class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

class BaseClass:
    arg = 'arg'

class MyBaseClass(BaseClass, metaclass=Singleton):
    pass

base_1 = BaseClass()
base_2 = BaseClass()
print(base_1.arg == base_2.arg)
print(base_1 != base_2.arg)

my_1 = MyBaseClass()
my_2 = MyBaseClass()
print(my_1.arg == my_2.arg)
print(my_1 == my_2)

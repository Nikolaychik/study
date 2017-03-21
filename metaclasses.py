class Meta(type):
    def __call__(self, *args, **kwargs):
        obj = type.__call__(self, *args)
        for name in kwargs:
            setattr(obj, name, kwargs[name])
        return obj


class InitMan:
    def __init__(self, **kwargs):
        for name in kwargs:
            setattr(self, name, kwargs[name])


class MetaMan:
    __metaclass__ = Meta


# meta_me = MetaMan(height=195, weight=80)
# init_me = InitMan(height=195, weight=80)
# men = [meta_me, init_me]
# for man in men:
#     print man.height
#     print man.weight


class META(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(META, cls).__new__(cls, name, bases, uppercase_attr)

class Foo:
    __metaclass__ = META
    bar = 'foo'

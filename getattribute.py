class GentleClass(object):
    def __getattribute__(self, item):
        if item[-7:] == '_please':
            return object.__getattribute__(self, item.split('_please')[0])
        else:
            raise AttributeError


GClass = GentleClass()
GClass.x = 'Some arg'
print(GClass.x_please)
print(GClass.x)

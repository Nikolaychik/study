class GentleClass(object):
    def __getattribute__(self, item):
        if '_please' in item:
            return object.__getattribute__(self, item.split('_please')[0])
        else:
            return "Say a magic word!"


GClass = GentleClass()
GClass.x = 'Some arg'
print(GClass.x)
print(GClass.x_please)

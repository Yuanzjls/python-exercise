# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

class Screen(object):
    """description of class"""
    @property
    def wh(self):
        return self.width,self.height
    @wh.setter
    def wh(self,args):
        self.width = args[0]
        self.height = args[1]
    @property
    def resolution(self):
        return self.width*self.height

s = Screen()
s.wh = (1024, 768)

print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print(self._path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

x = Chain().status.user.timeline.list


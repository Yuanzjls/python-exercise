#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
' a test module '

__author__ = 'Michael Liao'

import sys



def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

h = Hello()
h.hello()
print(type(Hello))
print(type(h))
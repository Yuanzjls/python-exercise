# -*- coding: utf-8 -*-
import re

def name_of_email(addr):
    m = re.match(r'<(.+)>',addr)
    if m!=None:
        return m.group(1)
    else:
        return re.match(r'^(\w+)\@(\w+).(\w+)$',addr).group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def product(*nums):
    if nums == ():
       raise TypeError
    pro = 1;
    for x in nums:
        pro = pro*x;
    return pro


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

def move(n,a='A',b='B',c='C'):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(2)


def trim(s):
    if s == '':
        return s
    count1 = 0
    while s[count1] == " ":
        count1 = count1 + 1;
        if count1 == len(s) :
            return ''
    count2 = len(s)-1
    while s[count2] == " ":
        count2 = count2 - 1
    s = s[count1:count2+1]
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试1失败!')
elif trim('  hello') != 'hello':
    print('测试2失败!')
elif trim('  hello  ') != 'hello':
    print('测试3失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试4失败!')
elif trim('') != '':
    print('测试5失败!')
elif trim('    ') != '':
    print('测试6失败!')
else:
    print('测试7成功!')

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    maxv = L[0]
    minv = L[0]
    for num in L:
        if maxv < num:
            maxv = num;
        if minv > num:
            minv = num;
    return (minv, maxv)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


def triangles():
    l = [1]
    while 1:
        yield l
        l = [1] + [ l[n] + l[n+1] for n in range(len(l)-1) ]  + [1] 



n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def prod(L):
    return reduce(lambda x, y: x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



def str2float(s):
    return reduce(lambda x, y: x + y / pow(10,len(s.split('.')[1])), map(float, s.split('.')))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

def is_palindrome(n):
    return str(n)[:] == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score, reverse = True)
print(L2)

def createCounter():
    def g():
        n = 0
        while True:
            n = n + 1
            yield n
    it = g()
    def counter():
        return next(it)
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


L = list(filter(lambda n:n%2==1, range(1, 20)))
print(L)

import time, functools
def metric(fn):
    t1 = time.time();
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, time.time()-t1))
        return fn(*args, **kw);
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')
__author__ = 'kby'
import random

b=[]
for i in range(5):
    x=random.randint(0,100)
    b.append(x)
print b[:3]
c=[]
for i in range(10):
    x=random.randint(0,50)
    c.append(x)
print c
c.sort()
print c
c=c[::-1]
print c
c.reverse()
print c
a=[random.randrange(0,100)for i in range(5)]
b=[]
for i in range(5):
    b.append(random.randrange(0,100))






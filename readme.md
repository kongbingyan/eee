__author__ = 'kby'
f=open("/home/kby/Downloads/testset.txt")
list=f.readlines()
m=len(list)
x1=[]
x2=[]
y=[]
for i in range(m):
    list[i]=list[i].strip().split(",")
    x1.append(int(list[i][0]))
    x2.append(int(list[i][1]))
    y.append(int(list[i][2]))
print x1,x2,y

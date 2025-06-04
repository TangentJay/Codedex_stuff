#dc warmup-novice
print(True*2-False*5) #2
print(int(6/10)*bool('python')+1) #1
print(3-int(3.2)) #0
print(bool(1)*int(4.2)+1) #5

print("6"*(2**2)) # the call ~ 6666
#print("6"**(2**2))
#print("6"+(2**2))

print(type(4))
print(4*5**2)
print(4*5**5)
print(4*5**3)

x=5
y=x
print(x+y)
print(x*y)
print(x**y)

x=[6,5,8,2,4,0]
print(x[5]+ x[2])

x= [4,5,6]
y=[-1,.1,1.1] + x[0:2]
print(sorted(y))

z=[7,8,9] 
d=[-3.3,-2,3.2] +z[0:2]
print(len(d))

e=[1,2,3]
g=[-1,.1,1.1] + e[0:2]
print(max(g))

x= [['a','b'],['c','d'],['f,e']]
print(x[0][1])

x.sort()

print(x)
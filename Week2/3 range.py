#range(start, stop, step)
#range start from 0
x = range (9)

for n in x :
    print(n)
    #will print 0 - 8

print("------------")
#range start from 3 stop in 6
x = range(3,6)
for n in x :
    print(n)
    #will print 3,4,5
print("------------")
#range start from 3 to 20, with intervl 2
x = range(3,20,2)
for n in x :
    print(n)
    #will print 3+2 to n (3-19)
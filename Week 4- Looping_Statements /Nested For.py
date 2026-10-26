# print word and its length without using len() in dictionary 
z='Rohit Sharma'
a=z.split()
d={}
for i in a:
    count=0   
    for j in i:
        count+=1
    d[i]=count
print(d)


#print words as key and vowel as value in dictionary 
z='Rohit Sharma'
a=z.split()
d={}
for i in a:
    vwl=''
    for j in i:
        if a[j] in "AEIOUaeiou":
            vwl+=vwl
    d[i]=vwl
print(d)


#a=[100,200,350,450]
#out=[1000,900,750,650]

a=[100,200,350,450]
out=[]
for i in a:
    s=0
    for j in a:
        if j!=i:
            s=s+j
    out.append(s)
print(out)
#or 
a=[100,200,350,450]
out=[]
for i in a:
    s=0
    for j in a:
        s=s+j
    out.append(s-i)
print(out)


#'pulav is love
#output= {'pulav': ['valup', 'plv', 2], 'is': ['si', 'i', 1], 'love': ['evol', 'lv', 2]}
a='pulav is love'
z=a.split()
out={}
for i in z:
    vwl=0
    for j in i:
        if j in 'AEIOUaeiou':
            vwl+=1
    out[i]=[i[::-1],i[::2],vwl]
print(out)
#or 
for i in z:
    vwl=0
    for j in i:
        l=[]
        if j in 'AEIOUaeiou':
            vwl+=1
    out[i]=l.append([i[::-1],i[::2],vwl])
print(out)


#out= {'python':'PyThOn...}
a=['python','outswing',10,45,4j+9,True, 'Java','Network',False,92.5]
d={}
for i in a:
    val=''
    if type(i)==str:
            for j in range(len(i)):
                if j%2==0:
                    val=val+i[j].upper()
                else:
                     val=val+i[j]
                d[i]=val
print(d)


# print less than given value seperatelly from greater than
a=[100,200,300,250,450,150,750]
s=300
less=[]
upp=[]
out=[]
for i in a:
    if i<s:
        less=less+[i]
    else:
        upp=upp+[i]
print(less,upp)
    


#Find Common Elements Between Two Lists
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]
# output = [30, 40, 50]
a=[10, 20, 30, 40, 50]
b=[30, 40, 50, 60, 70]
out=[]
for i in a:
    for j in b:
        if i==j:
            out+=[i]
print(out)
            


# Character Frequency Counter in a Sentence   
# a = "data science"
# output = {'d': 2, 'a': 2, 't': 1, 's': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1}
a='data science'
d={}
for i in a:
    count=0
    for j in a:
        if i==j:
            count+=1
    d[i]=count
print(d)


# Unique Pair Sum Finder
# a = [2, 4, 3, 5, 7, 8, -1]
# target = 7
# output = [[2, 5], [4, 3], [8, -1]]  (or similar pairs)
a = [2, 4, 3, 5, 7, 8, -1]
target = 7
pairs = []
for i in a:
    for j in a:
        if i+j==target:
            pairs.append([i,j])
print(pairs)



# Flatten a 2D List Without Built-in Methods
# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat_list = []
for i in matrix:
    for j in i:
        flat_list.append(j)
print(flat_list)



# Find Duplicate Characters in a Word
# word = "programming"
# output = ['r', 'g', 'm']  # (characters that repeat)
word = "programming"
duplicates = []
for i in word:
    count=0
    for j in word:
        if i==j:
            count+=1
    if count>1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)
    










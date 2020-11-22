print("Добро пожаловать!")
Loc=[[1,1,1,1,1,1,1,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,9,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,1,1]]
for i in Loc:
    print(i)
print("Загрузка...")
a=3
b=2
Loc[3][2]=5
for i in Loc:
    print(i)
c=input()
if (c.find("move_right(")!=-1):
    Loc[a][b]=0
    b=b+int(c[11:len(c)-1])
    Loc[a][b]=5
for i in Loc:
    print(i)
#print(Loc[1])
#print(Loc[2])
#print(Loc[3])
#print(Loc[4])
#print(Loc[5])
#print(Loc[6])
#print(Loc[7])

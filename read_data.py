

data = open("file_name.txt", "r")
data = data.read()
data = data.split("\n")
data = [x for x in data if x!='']

data = [int(x) for x in data]


potega3=[]
for i in range(1, 100000):
  p=3**i
  if p <100000 and p not in potega3:
    potega3.append(p)
  
  
for liczba in data:
  if liczba in potega3:
    print(liczba)

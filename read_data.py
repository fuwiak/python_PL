

data = open("file_name.txt", "r")
data = data.read()

potega3=[]
for i in range(1, 100000):
  p=i**3
  if p <100000 and p not in potega3:
    potega3.append(p)
  

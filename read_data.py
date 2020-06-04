potega3=[]
for i in range(1, 100000):
  p=3**i
  if p <100000 and p not in potega3:
    potega3.append(p)
  
 

def silnia(n):
  if n==0 or n==1:
    return 1
  else:
    return silnia(n-1)*n
  
#read the file
data = open("file_name.txt", "r")
data = data.read()
data = data.split("\n")
data = [x for x in data if x!='']

data = [int(x) for x in data]

for liczba in data:
  if liczba in potega3:
    print(liczba)
  
  
temp_sum=[]
for liczba in data:
  splitted_number = str(liczba).split("")
  for num in splitted_number:
    num = int(num)
    if num == silnia(num):
      temp_sump.append(num)
 
 
      
    
  
  
  
  
  
  

#petla for, while

lista = [1,2,3,8]


#wypisanie wszystkich elementow listy
for liczba in lista:
  print(liczba)
  

#wypisane tylko parzystych elementow listy

for liczba in lista:
  if liczba%2==0:
    print(liczba)
    
#wypisanie elementow listy wraz z jej indexami

for ind, num in enumerate(lista):
  print(ind, num)

# if-else-elif 


#1 
a,b,c = 1,2,1

delta=b**2 -4*a*c

if delta>0:
  print("2 rozwiazania w zbiorze liczb rzeczywistych")
elif delta == 0:
  print("1 rozwiazanie w zbiorze liczb rzeczywistych")
else:
  print("Brak rozwiazan")
  
#2

number=9

if number>=0:
  print("Liczba jest nieujemna")
else:
  print("Liczba jest ujemna")
  
# listy

lista = [1,2,3,-1,2]

print(lista[0]) # pierwszy element listy, w naszym przypadku do bedzie liczba 1
print(lista[-1]) # ostatni element listy ---> 2
print(lista[-2]) # przedostatni elemt listy

lista[::-1] # odwrotna kolejnosc listy

lista[::2 ] # co drugi element 

lista[::2] #to jest rownowazne lista[0::2]

lista[1::2] # zaczynamy od elementu z indexem rownym 1(tzn w drugi w kolejnosc) i wtedy zaczynamy brac co druga element 

lista[2:6] # wycinamy liste od indexu 2 do indexu 5( 6-1)


# lista list 

A = [[1,2,3], [4,5,6], [7,8,9]]
  









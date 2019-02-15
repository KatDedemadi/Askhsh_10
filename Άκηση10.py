#Άσκηση 10
#Γράψτε ένα πρόγραμμα το οποίο επισκέπτεται μία ιστοσελίδα HTML που παίρνει
#από τον χρήστη και βρίσκει πόσοι σύνδεσμοι υπάρχουν και πόσες αλλαγες 
#γραμμής (έιτε από br είτε από p).

import urlib.request
from bs4 import BeautifulSoup

url= input("Dwse mou to URL ths istoselidas.")

#Χρήση βιβλιοθήκης για να παρουμε το ulr απο τον χρηστη

with urlib.request.urlopen(url) as response:
    html= response.read()

soup=BeautifulSoup(html,"html.parser")

#Εύρεση συνδέσμων που υπαρχουν μέσα στο url που δωθηκε από τον χρήστη 
syndesmoi= []
for synd in soup.find_all('a'):
    syndesmoi.append(synd)
print("Oi syndesmoi poy vrethikan einai:"+len(syndesmoi))

#Γενική κταμέτρηση αλλαγών σειράς
allages_seiras= []
#Εύρεση αλλαγών σειράς με <br>
for allagh_s in soup.find_all("br"):
    allages_seiras.append(allagh_s)

#Εύρεση αλλαγών σειράς με <p>.
for  allagh_p in soup.find_all("p"):
    allages_seiras.append(allagh_p)
#Εμφάνηση αποτελέσματος
print("Oi allages seiras pou vrethikan einai:" +len(allages_seiras))




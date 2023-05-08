import requests
from bs4 import BeautifulSoup
import csv


# Adres URL witryny z listą cytatów Marka Aureliusza
url = 'https://imperiumromanum.pl/kultura/zlote-mysli-rzymian/cytaty-marka-aureliusza/'


# Wysłanie zapytania HTTP i pobranie strony internetowej
response = requests.get(url)
print(response.status_code)
html_content = response.content.decode('utf-8')

# Analiza HTML i zidentyfikowanie interesujących elementów
soup = BeautifulSoup(html_content, 'html')
quotes = soup.find("ul", class_="cyt").find_all("li", recursive=False)

my_quotes = []

for quote in quotes:
    my_quotes.append(quote.text)
   
    


# otwarcie pliku csv w trybie w+_
file = open('golden_quotes.csv', 'w+',newline='', encoding='utf-8')

# zapisanie danych do pliku csv
with file: 
    write = csv.writer(file)
    write.writerow(my_quotes)








    

    








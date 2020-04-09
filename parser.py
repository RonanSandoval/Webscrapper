import requests
from bs4 import BeautifulSoup 


with open("Algonquian Linguistics Atlas.html", "r") as f:
    content = f.read()
soup = BeautifulSoup(content ,'html.parser')
print(soup.prettify())

categories = soup.find(id = "categoryList")

print(categories)

import requests
from bs4 import BeautifulSoup 

page = requests.get("https://www.atlas-ling.ca/app")
soup = BeautifulSoup(page.content ,'html.parser')
print(soup.prettify())

categories = soup.find(id = "categoryList")

print(categories)


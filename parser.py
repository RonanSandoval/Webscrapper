import requests
from bs4 import BeautifulSoup 


with open("Algonquian Linguistics Atlas.html", "r") as f:
    content = f.read()
soup = BeautifulSoup(content ,'html.parser')

soupCategories = soup.find(id = "categoryList")

# categories are obtained
categories = []

for item in soupCategories.contents[1]:
    categories.append(item.getText())

print(categories)

# phrases are obtained
soupMeaninglist = soup.find_all(id = "meaningList")

meaningList = []

for item in soupMeaninglist[1].contents[2]:
    meaningList.append(item.getText())

print(meaningList)






import urllib2
from bs4 import BeautifulSoup 

page = urllib2.urlopen("https://www.atlas-ling.ca/app")
soup = BeautifulSoup(page,'html.parser')

categories = soup.select("div", {"id" : "categoryList"})
    #{"class:", "list-group-item p-0"})
#vals = app.find("div", {"class" : "list-group-item"})
print(categories.contents)


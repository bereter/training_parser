import requests
from bs4 import BeautifulSoup

url = "https://jetlend.ru/borrower/"

req = requests.get(url)

src = req.text

soup = BeautifulSoup(src, "lxml")


tags = [i.name for i in soup.find_all()]
print(len(tags))
attributes = [i.attrs for i in soup.find_all() if len(i.attrs) > 1]


print(attributes)
sum_attributes = 0
for i in soup.find_all():
    if len(i.attrs) > 1:
        sum_attributes += 1
print(len(attributes))
def tags_attributes():
    tags = [i.name for i in soup.find_all()]
    attributes = [i.attrs for i in soup.find_all() if len(i.attrs) > 1]
    return f"HTML тегов - {len(tags)}, из них содержат атрибуты - {len(attributes)}"


print(tags_attributes())






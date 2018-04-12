import requests
from bs4 import BeautifulSoup
import csv
mainData=[]

url='http://www.ucl.ac.uk/prospective-students/accommodation/residences/houses'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
arts=soup.find('tbody')
articles=arts.find_all('tr')

for article in articles:
    name=article.find('td','align-left all-vp name').getText().strip()
    distance=article.find('td','align-left extra').getText().strip().replace("\r\n",'').replace(" ",'')
    meta=article.find('td','align-left all-vp name').find('a')
    links=meta.get('href')


    res=requests.get(links)
    soup=BeautifulSoup(res.text,'lxml')
    arts2=soup.find('tbody')
    articles2=arts2.find_all('tr','even')
    
    for article2 in articles2:
        roomtype=article2.find('span','roomtype').getText().strip()
        other=article2.find_all('td')
        rate=other[1].text.replace('£','')
        number=other[2].text
        print(name,distance,roomtype,rate,number)
        
        itemall={'name':name,'distance':distance,'roomtype':roomtype,'rate':rate,'number':number}
        mainData.append(itemall)




with open('get_ucldorm03.csv','w') as csvfile:
    fieldnames=['name','distance','roomtype','rate','number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for item in mainData:
        print (item)
        writer.writerow(item)

print("Writing csv complete")


""" #If you want to scrape a website:
#1.Can use API
#2.HTML Web Scrapping using some tools like bs4

#Step 0 : Install All required libraries
#libraries: bs4,requests,html5lib
 """


 
import requests
from bs4 import BeautifulSoup
url = 'https://www.codewithharry.com/'

#Step1: Get the HTML

r = requests.get (url)
htmlContent = r.content
#print(htmlContent) 

#Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

""" #step 3: HTML Tree Traversal
#types of objects commonly used
print(type(title)) #1.Tag 
print(type(title.string)) #2.Navigable string
print(type(soup)) #3.BeautifulSoup
#4.comments """

#get the title of the HTML page
title = soup.title

#Get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)

#Get all the Anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link!='#'):
       all_links.add("https://www.codewithharry.com/ " +link.get('href'))
#print(anchors)

# Get first element in the HTML
print(soup.find('p') 

# Get classes of any element in the HTML
#print(soup.find('p')['class'])

# find all the elements with class lead
#print(soup.find_all("p", class_="lead"))

#get the tags from soup /tags
#print(soup.find('p').get_text())

#print (all_links)
#first we will make a request to the webpage we want to scrape . pass it to beautiful soup 


import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep # will help us to include a halt of few seconds before making another request
all_quotes= []#a dictionary that will later store quotes author name etc.
base_url = "http://quotes.toscrape.com/"
url = "/page/1"

while url:
    res = requests.get(f"{base_url}{url}")
    print(f"RIGHT NOW WE ARE SCRAPING : {base_url}{url}")
    souped = BeautifulSoup(res.text,features="lxml")
#print(souped)#we get the html page
#now we want al items with class quotes
    quotes = souped.find_all(class_="quote")#now loop thru all quotes
#focus on text its located inside a span

    for quote in quotes:
     all_quotes.append({
          "Quote":quote.find(class_="text").get_text(),
          "Author":quote.find(class_="author").get_text(),
          "Link": quote.find("a")["href"]
         })
   # print(all_quotes)#prints a list of dictionaries with quote authorname and link
    #this only prints a result of one page now we want information from eah page
    # we see a next button at the bottom right corner of the page where the quotes end above the top ten tags
    #we will try and use it
    nextbutton = souped.find(class_="next")
    url = nextbutton.find("a")['href'] if nextbutton else None#go onto nextbutton
    #sleep(2)#a halt of two second before another request is made
quote = choice(all_quotes)
print("Here is a quote for you :")
print(quote["Quote"])
print("The author of the quote is")
print(quote["Author"])



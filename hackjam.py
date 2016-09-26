'''Ian Galbraith
HackJam 9/24/16'''
import urllib 
import urllib.request
import html.parser
from html.parser import *
import re
import sys
#get BeautifulSoup not really necessary for this proj but is super cool
from bs4 import BeautifulSoup
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/48.0')]
#Creating a request and making the request seem like it's Firefox
url = input("Provide an Amazon webpage: ")
#Taking in a url
handle = opener.open(url)
html = handle.read()
#opening and reading and right now it's in data form
def Amazonchecker(html):
   matches = re.findall('"reviewCountTextLinkedHistogram noUnderline"', str(html));
   if len(matches) == 0: 
      return False
   else:
      return True
boolcheck = Amazonchecker(html)
if boolcheck == False:
   sys.exit("You didn't put in an Amazon website")
#checks to ensure that's it's amazon website 
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify()) Never print this or rip PC
sitetext = soup.get_text()
t = sitetext.index("out of")
#print(t)
#String slicing to print out the rating
print(sitetext[t-10:t+15])

'''
Useful part is probably only getting HTML right now
'''

'''
implementation for future text files?
for line in sitetext:
    if "out of" in line:
       print (line)
   '''    

#Fix this part :(
'''
urltext = []
#Creating the HTML Parser
class parseText(html.parser.HTMLParser):
#Define a custom parseText class as specialization of the html.parsers.HTMLParser class
    def data_handler(self,data):
        if data != '\n':
            urlText.append(data)

#Creating an instance of the parser
amazonparser = parseText()
amazonparser.feed(urllib.request.urlopen(url).read())
amazonparser.close()
#Printing out the text
for x in urltext:
    print (x)
'''


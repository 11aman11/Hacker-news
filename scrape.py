import requests # allows us to download the html file data
from bs4 import BeautifulSoup # allows us to scrap the data the way that you want
import pprint
res=requests.get("https://news.ycombinator.com/") #here trying to grab the infromation of the website using request
#print(res.text) # 200 status and give u the entire html text file and now we can use the beautiful soup to grab the data you want

soup =BeautifulSoup(res.text,"html.parser")# now we parse it and we only care abou tht news(text) not the css file for styling or images
#print(soup.body) # to grab the body only!
#print(soup.find_all("a")) #get all th links
#print(soup.find("title")) # gives the 1st title
#print(soup.select(".score")) # allows us to grab the elements of html css selectors ex: we grabbed all the score points
#print(soup.select(".titlelink")[0]) #grabs the first link
links = soup.select(".titlelink")
subtext = soup.select(".subtext")



def createCustom(links,votes):
    list=[]
    for i,item in enumerate(links):
        title=item.getText() # only title
        href= item.get("href",None) # only links
        votes=subtext[i].select(".score")
        if len(votes):
            points= int(votes[0].getText().replace(" points","")) # just getting the numbers
            #print(points)
            if points >= 100:
                list.append({"title":title,"link":href,"votes":points})
    return sortStoriesByVotes(list)

def sortStoriesByVotes(list):
    return sorted(list, key=lambda k:k["votes"],reverse=True) # this allows us to sort the list with dicts n with top votes

pprint.pprint(createCustom(links,subtext))

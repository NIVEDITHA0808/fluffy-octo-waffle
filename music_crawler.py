import requests
import bs4

# modification in output(beautify) using prettify()

#resp = requests.get("https://www.metrolyrics.com/in-my-feelings-lyrics-drake.html")

#soup = bs4.BeautifulSoup(resp.content,features="lxml")

#print(soup.prettify())
'''
# normal output
resp = requests.get("https://www.metrolyrics.com/in-my-feelings-lyrics-drake.html")

soup = bs4.BeautifulSoup(resp.content)

print(soup)

# if the source is stored as html file
f= open('simple.html','r')
soup = bs4.BeautifulSoup(f,'lxml') 
print(soup)
'''
# urls in the website
def get_links(url):
    link=[]
    
    resp = requests.get(url)

    soup = bs4.BeautifulSoup(resp.content,features="lxml")

    links = soup.find_all("a", attrs={"class":"title"} )

    for i in links:
        link.append(i['href'])
    print(link)
    
get_links("https://www.metrolyrics.com/in-my-feelings-lyrics-drake.html")


def make_file(url):
    return(url.split("/")[-1].replace(".html","txt")
 
def lyrics_title(url):
    resp = requests.get(url)

    soup = bs4.BeautifulSoup(resp.content,features="lxml")
    
    title = soup.find('title')

    match = soup.title.text
        
    print(match)

lyrics_title("https://www.metrolyrics.com/in-my-feelings-lyrics-drake.html")
     
def get_lyrics(url):
    resp = requests.get(url)

    soup = bs4.BeautifulSoup(resp.content,features="lxml")
    
    part = soup.find('div',attrs={"class":"js-lyric-text"})

    for para in part.find_all('p',attrs={"class":"verse"}): 
        match = para.text
        
        print(match)
        
get_lyrics("https://www.metrolyrics.com/in-my-feelings-lyrics-drake.html")


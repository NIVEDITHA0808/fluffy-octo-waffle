import requests
import bs4

def get_links(url):
    link=[]
    
    resp = requests.get(url)

    soup = bs4.BeautifulSoup(resp.content,features="lxml")

    links = soup.find_all("a", attrs={"class":"title"} )

    for i in links:
        fname = make_file(url)
        f = open('fname','w')
        lyrics = get_lyrics(i)
        f.write(lyrics)
        f.close()
        
def make_file(url):
    return(url.split("/")[-1].replace(".html","txt")
    
    
def get_lyrics(url):
    lyrics = []
    resp = requests.get(url)

    soup = bs4.BeautifulSoup(resp.content,features="lxml")
    
    part = soup.find('div',attrs={"class":"js-lyric-text"})

    for para in part.find_all('p',attrs={"class":"verse"}): 
        lyrics.append(para.get_text())
        return "\n".join(lyrics)
        
def main():
       
    links = get_links("https://www.metrolyrics.com/drake-lyrics.html")
    for i in links:
        fname = make_file(url)
        print(f"{i}->{fname}")
        f = open('fname','w')
        lyrics = get_lyrics(i)
        f.write(lyrics)
        f.close()
        

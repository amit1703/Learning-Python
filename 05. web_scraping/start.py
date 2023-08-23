import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")#getting the site view source with requests

soup = bs4.BeautifulSoup(res.text, 'lxml')

print(soup.select('title')[0].getText())#scraping with bs4 the title
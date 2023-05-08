import bs4
import requests

url = "https://dictionary.cambridge.org/ja/dictionary/english/"

word = input("Enter an English word")

wurl = url + word
headers_dic = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

site = requests.get(wurl,headers=headers_dic,timeout=(7.0,7.5))

soup = bs4.BeautifulSoup(site.content, "html.parser")
tests = soup.find("div",class_="def ddef_d db")

print(tests.text)

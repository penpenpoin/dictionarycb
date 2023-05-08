import bs4
import requests

url = "https://dictionary.cambridge.org/ja/dictionary/english/"
headers_dic = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

word = input("Enter an English word")
words = word.split() ##空欄で単語を区切る
for word in words:
	wurl = url + word

	site = requests.get(wurl,headers=headers_dic,timeout=(7.0,7.5))

	soup = bs4.BeautifulSoup(site.content, "html.parser")
	tests = soup.find("div",class_="def ddef_d db")

	if tests is None :
		print("something went wrong")
		continue
	print(tests.text)
